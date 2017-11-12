from marshmallow import Schema, fields, validates, post_dump, missing
from marshmallow.validate import OneOf
from .fields import StrippedString


class AttributeDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class BaseSchema(Schema):
    
    def on_bind_field(self, field_name, field_obj):
        if field_obj.missing == missing:
            field_obj.missing = None
            field_obj.allow_none = True

    @post_dump
    def clean_missing(self, data):
        ret = data.copy()
        for key in filter(lambda key: data[key] is None, data):
            del ret[key]
        return ret

    @property
    def dict_class(self):
        return AttributeDict


class BoundingBoxSchema(BaseSchema):
    latitude_min = fields.Float()
    latitude_max = fields.Float()
    longitude_min = fields.Float()
    longitude_max = fields.Float()


class BaseRequestSchema(BaseSchema):
    area = fields.String()
    street = fields.String()
    town = fields.String()
    postcode = fields.String()
    county = fields.String()
    country = fields.String()
    latitude = fields.String()
    longitude = fields.String()
    lat_min = fields.String()
    lat_max = fields.String()
    lon_min = fields.String()
    lon_max = fields.String()
    output_type = fields.String()


class BaseResultSchema(BaseSchema):
    area_name = StrippedString()
    street = fields.String()
    town = fields.String()
    postcode = fields.String()
    country = fields.String()
    county = fields.String()
    bounding_box = fields.Nested(BoundingBoxSchema)


class SearchPropertyListingRequestSchema(BaseRequestSchema):
    radius = fields.Float()
    order_by = fields.String(validate=OneOf(choices=('price', 'age')))
    ordering = fields.String(validate=OneOf(choices=('descending', 'ascending')))
    listing_status = fields.String(validate=OneOf(choices=('rent', 'sale')))
    include_sold = fields.String(validate=OneOf(choices=('0', '1')))
    include_rented = fields.String(validate=OneOf(choices=('0', '1')))
    minimum_price = fields.Float()
    maximum_price = fields.Float()
    minimum_beds = fields.Integer()
    maximum_beds = fields.Integer()
    furnished = fields.String()
    property_type = fields.String(validate=OneOf(choices=('houses', 'flats')))
    new_homes = fields.String()
    chain_free = fields.String()
    keywords = fields.String()
    listing_id = fields.String()
    branch_id = fields.String()
    page_number = fields.Integer()
    page_size = fields.Integer()
    summarised = fields.String(validate=OneOf(choices=('yes', 'no')))

    @validates('radius')
    def validate_radius(self, value):
        return 0.1 < value < 40


class PropertyListingSchema(BaseSchema):
    class Meta:
        dateformat = '%Y-%m-%d %H:%M:%S'

    listing_id = fields.String()
    listing_status = fields.String()

    price = fields.Float()

    agent_address = fields.String()
    agent_logo = fields.URL()
    agent_name = fields.String()
    agent_phone = fields.String()

    category = fields.String()
    country = fields.String()
    country_code = fields.String()
    county = fields.String()

    description = fields.String()
    details_url = fields.URL()
    displayable_address = fields.String()
    first_published_date = fields.DateTime()
    last_published_date = fields.DateTime()

    image_url = fields.String()

    latitude = fields.Float()
    longitudine = fields.Float()

    num_bathrooms = fields.Integer()
    num_bedrooms = fields.Integer()
    num_receptions = fields.Integer()
    outcode = fields.String()
    post_town = fields.String()
    property_tipe = fields.String()
    street_name = fields.String()


class PropertyListingResultSchema(BaseResultSchema):
    listing = fields.Nested(PropertyListingSchema, many=True)
    result_count = fields.Integer()


class LocalInfoGraphsResultSchema(BaseResultSchema):
    people_graph_url = fields.Url()
    crime_graph_url = fields.Url()
    council_tax_graph_url = fields.Url()
    education_graph_url = fields.Url()


class ZedIndexRequestSchema(BaseRequestSchema):
    output_type = fields.String(validate=OneOf(choices=(
        'town', 'outcode', 'county', 'country'
    )))


class ZedIndexResultSchema(BaseResultSchema):
    area_url = fields.String()
    zed_index = fields.Integer()
    zed_index_3month = fields.Integer()
    zed_index_6month = fields.Integer()
    zed_index_1year = fields.Integer()
    zed_index_2year = fields.Integer()
    zed_index_3year = fields.Integer()
    zed_index_4year = fields.Integer()
    zed_index_5year = fields.Integer()


class ZedIndicesResultSchema(BaseSchema):
    name = fields.String()
    latitude = fields.Float()
    longitude = fields.Float()
    zed_index = fields.Integer()


class AreaZedIndicesRequestSchema(BaseRequestSchema):
    ordering = fields.String(
        validate=OneOf(choices=('descending', 'ascending')))
    page_number = fields.Integer()
    page_size = fields.Integer()
    area_type = fields.String(validate=OneOf(choices=(
        'streets', 'postcodes', 'outcodes', 'areas', 'towns', 'counties'
    )))


class AreaZedIndicesResultSchema(BaseResultSchema):
    results_url = fields.Url()
    result_count = fields.Integer()
    results = fields.Nested(ZedIndicesResultSchema, many=True)


class SuggestionSchema(BaseSchema):
    value = fields.String()
    identifier = fields.String(allow_none=True)


class AutocompleteRequestSchema(BaseRequestSchema):
    search_term = fields.String()
    search_type = fields.String(validate=OneOf(choices=(
        'listings', 'properties'
    )))


class AutoCompleteResultSchema(BaseResultSchema):
    suggestions = fields.Nested(SuggestionSchema, many=True)


class AreaValueGraphsRequestSchema(BaseRequestSchema):
    size = fields.String()
    output_type = fields.Constant('outcode')


class AreaValueGraphsResultSchema(BaseResultSchema):
    area_values_url = fields.Url()
    home_values_graph_url = fields.Url()
    value_trend_graph_url = fields.Url()
    value_ranges_graph_url = fields.Url()
    average_values_graph_url = fields.Url()


class AverageAreaSoldPriceResultSchema(BaseResultSchema):
    average_sold_price_1year = fields.Float()
    average_sold_price_3year = fields.Float()
    average_sold_price_5year = fields.Float()
    average_sold_price_7year = fields.Float()
    number_of_sales_1year = fields.Integer()
    number_of_sales_3year = fields.Integer()
    number_of_sales_5year = fields.Integer()
    number_of_sales_7year = fields.Integer()
    turnover = fields.Float()
    prices_url = fields.Url()


class AverageSoldPriceRequestSchema(BaseRequestSchema):
    area_type = fields.String(validate=OneOf(choices=(
        'streets', 'postcodes', 'outcodes', 'areas', 'towns', 'counties'
    )))
    page_number = fields.Integer()
    page_size = fields.Integer()
    ordering = fields.String(
        validate=OneOf(choices=('descending', 'ascending')))


class AverageSoldPricesBaseResultSchema(BaseResultSchema):
    result_count = fields.Integer()
    result = fields.Nested(AverageAreaSoldPriceResultSchema, many=True)


class RefineEstimateSchema(BaseSchema):
    property_id = fields.Integer()
    property_type = fields.String(validate=OneOf(choices=(
        'detached',
        'link_detached',
        'semi_detached',
        'terraced',
        'flat',
        'end_terrace',
        'maisonette',
        'mews',
        'town_house',
        'cottage',
        'bungalow',
        'farm_barn',
        'park_home'
    )))
    tenure = fields.String(validate=OneOf(choices=(
        'freehold',
        'leasehold',
        'share_of_freehold'
    )))
    num_bedrooms = fields.Integer()
    num_bathrooms = fields.Integer()
    num_receptions = fields.Integer()
    session_id = fields.String()


class RefineEstimateResultSchema(BaseSchema):
    estimate = fields.String()
    upper_estimate = fields.String()
    lower_estimate = fields.String()
    confidence = fields.Integer()


class ArrangeViewingSchema(BaseSchema):
    session_id = fields.String()
    message = fields.String()
    best_time_to_call = fields.String(validate=OneOf(choices=(
        'anytime',
        'afternoon',
        'evening',
        'morning'
    )))
    phone_type = fields.String(validate=OneOf(choices=(
        'mobile',
        'work',
        'home',
        'morning'
    )))
    phone = fields.String()
    email = fields.Email()
    name = fields.String()
    listing_id = fields.Integer()


class ArrangeViewingResultSchema(BaseSchema):
    success = fields.Integer()
    error = fields.String()
