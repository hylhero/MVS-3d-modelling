from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
import sys
import LatLongUTMconversion as con

#function to get photos from the directory
def getPhotosFromDirectory(photoDir):
    return[f for f in os.listdir(photoDir) if os.path.isfile(os.path.join(photoDir, f)) and os.path.splitext(f)[1].lower()==".jpg"]

 
def get_exif_data(image):
    """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for gps_tag in value:
                    sub_decoded = GPSTAGS.get(gps_tag, gps_tag)
                    gps_data[sub_decoded] = value[gps_tag]
 
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
 
    return exif_data
	
def _convert_to_degress(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    deg_num, deg_denom = value[0]
    d = float(deg_num) / float(deg_denom)
 
    min_num, min_denom = value[1]
    m = float(min_num) / float(min_denom)
 
    sec_num, sec_denom = value[1]
    s = float(sec_num) / float(sec_denom)
    
    return d + (m / 60.0) + (s / 3600.0)
 
def get_lat_lon(exif_data):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    lat = None
    lon = None
    alt=None
 
    if "GPSInfo" in exif_data:		
        gps_info = exif_data["GPSInfo"]
 
        gps_latitude = gps_info.get("GPSLatitude")
        gps_latitude_ref = gps_info.get('GPSLatitudeRef')
        gps_longitude = gps_info.get('GPSLongitude')
        gps_longitude_ref = gps_info.get('GPSLongitudeRef')
        gps_altitude=gps_info.get('GPSAltitude')
        gps_altitude_ref=gps_info.get('GPSAltitudeRef')
        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":                     
                lat *= -1
 
            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon *= -1
        altn,altd=gps_altitude
        alt=float(altn)/float(altd)
        
    return lat, lon,alt
 
 
################
# Example ######
################
if __name__ == "__main__":
    # load an image through PIL's Image object
    if len(sys.argv) < 2:
        print "Error! No image file specified!"
        print "Usage: %s <filename>" % sys.argv[0]
        sys.exit(1)
    inp=open(sys.argv[2],"w")
    p=getPhotosFromDirectory(sys.argv[1])
    for path in p:
        #print(path)
        photopath=os.path.join(sys.argv[1],path)
        #print photopath
        photoHandle = Image.open(photopath)        
        exif_data = get_exif_data(photoHandle)
        lat,lon,alt=get_lat_lon(exif_data)
              
        if lat==None or lon==None or alt==None:
            inp.write("none none none")
            inp.write('\n')
            
        else:
            (z, e, n) = con.LLtoUTM(23,lon,lat)
            inp.write(str(e)+'\t'+str(n)+'\t'+str(alt)+'\n')
            
