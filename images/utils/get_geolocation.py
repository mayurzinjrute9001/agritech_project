from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_geolocation(image_file):
    """
    Extract geolocation (latitude, longitude) from an image's EXIF data.
    Returns (latitude, longitude) as floats or (None, None) if not available.
    """
    try:
        img = Image.open(image_file)
        exif_data = img._getexif()

        if not exif_data:
            return None, None

        gps_info = {}
        for tag, value in exif_data.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_info = value
                break

        if not gps_info:
            return None, None

        def _convert_to_degrees(value):
            d, m, s = value
            return d + (m / 60.0) + (s / 3600.0)

        lat = gps_info.get(2)  # GPSLatitude
        lat_ref = gps_info.get(1)  # GPSLatitudeRef
        lon = gps_info.get(4)  # GPSLongitude
        lon_ref = gps_info.get(3)  # GPSLongitudeRef

        if lat and lon and lat_ref and lon_ref:
            latitude = _convert_to_degrees(lat)
            if lat_ref != "N":
                latitude = -latitude

            longitude = _convert_to_degrees(lon)
            if lon_ref != "E":
                longitude = -longitude

            return latitude, longitude
    except Exception:
        return None, None

    return None, None
