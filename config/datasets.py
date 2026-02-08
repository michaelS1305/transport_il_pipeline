DATASETS = [
    {
        "name": "car_plate_numbers",
        "api_url": "https://data.gov.il/api/3/action/datastore_search",
        "resource_id": "053cea08-09bc-40ec-8f7a-156f0677aff3",
        "catalog": "transport_lakehouse",
        "schema": "bronze",
        "table": "car_plate_numbers_raw",
        "load_type": "full",
        "enabled": True
    },
    {
        "name": "two_wheeled_plate_numbers",
        "api_url": "https://data.gov.il/api/3/action/datastore_search",
        "resource_id": "bf9df4e2-d90d-4c0a-a400-19e15af8e95f",
        "catalog": "transport_lakehouse",
        "schema": "bronze",
        "table": "two_wheeled_plate_numbers_raw",
        "load_type": "full",
        "enabled": True
    },
    {
        "name": "public_transport_plate_numbers",
        "api_url": "https://data.gov.il/api/3/action/datastore_search",
        "resource_id": "cf29862d-ca25-4691-84f6-1be60dcb4a1e",
        "catalog": "transport_lakehouse",
        "schema": "bronze",
        "table": "public_transport_plate_numbers_raw",
        "load_type": "full",
        "enabled": True
    },
    {
        "name": "electric_car_amount_per_region",
        "api_url": "https://data.gov.il/api/3/action/datastore_search",
        "resource_id": "07421a4e-5b12-4444-9173-5ca297b31f79",
        "catalog": "transport_lakehouse",
        "schema": "bronze",
        "table": "electric_car_amount_per_region_raw",
        "load_type": "full",
        "enabled": True
    }
]
