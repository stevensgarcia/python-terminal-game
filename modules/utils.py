from datetime import datetime

# Custom JSON encoder to handle datetime objects when serializing
# JSON objects
def datetime_encoder(obj):
  if isinstance(obj, datetime):
    return obj.isoformat()