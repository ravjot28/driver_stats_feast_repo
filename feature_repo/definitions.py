from google.protobuf.duration_pb2 import Duration
from feast import FeatureService, FeatureView, Field, FileSource, RequestSource, PushSource
from feast.types import Float32, Int64
from feast.value_type import ValueType
from feast.entity import Entity
from datetime import timedelta

# Declaring an entity for the dataset
driver = Entity(
    name="driver_id", 
    value_type=ValueType.INT64, 
    description="The ID of the driver"
    )

# Declaring the source for raw feature data
file_source = FileSource(
    path=r"/Users/singhra/Desktop/feature-store/driver_stats/feature_repo/data/driver_stats_with_string.parquet",
    timestamp_field="event_timestamp"
)

# Defining the features in a feature view
driver_stats_fv = FeatureView(
    name="driver_stats_fv",
    ttl=timedelta(seconds=86400 * 2),
    entities=[driver],
    schema=[
        Field(name="conv_rate", dtype=Float32),
        Field(name="acc_rate", dtype=Float32),
        Field(name="avg_daily_trips", dtype=Float32)        
        ],    
    source=file_source
)