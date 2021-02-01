import uuid
import random
import string
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField

PRODUCT_VEHICLE = 'VEHICLE'
PRODUCT_ACCESSORY = 'ACCESSORY'
ORDER_VIRTUAL = 'VIRTUAL'
ORDER_PROCESSING = 'PROCESSING'
ORDER_COMPLETED = 'COMPLETED'
ORDER_CANCELLED = 'CANCELLED'


CITY_CHOICES = (
    ('Agartala', 'Agartala'),
    ('Agra', 'Agra'),
    ('Agumbe', 'Agumbe'),
    ('Ahmedabad', 'Ahmedabad'),
    ('Aizawl', 'Aizawl'),
    ('Ajmer', 'Ajmer'),
    ('Alappuzha Beach', 'Alappuzha Beach'),
    ('Allahabad', 'Allahabad'),
    ('Alleppey', 'Alleppey'),
    ('Almora', 'Almora'),
    ('Amarnath', 'Amarnath'),
    ('Amravati', 'Amravati'),
    ('Amritsar', 'Amritsar'),
    ('Anantagir', 'Anantagir'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Araku valley', 'Araku valley'),
    ('Aurangabad', 'Aurangabad'),
    ('Ayodhya', 'Ayodhya'),
    ('Badrinath', 'Badrinath'),
    ('Bangalore', 'Bangalore'),
    ('Baroda', 'Baroda'),
    ('Bastar', 'Bastar'),
    ('Bhagalpur', 'Bhagalpur'),
    ('Bhilai', 'Bhilai'),
    ('Bhimtal', 'Bhimtal'),
    ('Bhopal', 'Bhopal'),
    ('Bhubaneswar', 'Bhubaneswar'),
    ('Bhuj', 'Bhuj'),
    ('Bidar', 'Bidar'),
    ('Bilaspur', 'Bilaspur'),
    ('Bodh Gaya', 'Bodh Gaya'),
    ('Calicut', 'Calicut'),
    ('Chail', 'Chail'),
    ('Chamba', 'Chamba'),
    ('Chandigarh', 'Chandigarh'),
    ('Chennai', 'Chennai'),
    ('Chennai Beaches', 'Chennai Beaches'),
    ('Cherai', 'Cherai'),
    ('Cherrapunji', 'Cherrapunji'),
    ('Chidambaram', 'Chidambaram'),
    ('Chikhaldara Hills', 'Chikhaldara Hills'),
    ('Chopta', 'Chopta'),
    ('Coimbatore', 'Coimbatore'),
    ('Coonoor', 'Coonoor'),
    ('Coorg', 'Coorg'),
    ('Corbett National Park', 'Corbett National Park'),
    ('Cotigao Wild Life Sanctuary', 'Cotigao Wild Life Sanctuary'),
    ('Cuddalore', 'Cuddalore'),
    ('Cuttack', 'Cuttack'),
    ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'),
    ('Dalhousie', 'Dalhousie'),
    ('Daman and Diu', 'Daman and Diu'),
    ('Darjeeling', 'Darjeeling'),
    ('Dehradun', 'Dehradun'),
    ('Delhi', 'Delhi'),
    ('Devikulam', 'Devikulam'),
    ('Dhanaulti', 'Dhanaulti'),
    ('Dharamashala', 'Dharamashala'),
    ('Dindigul', 'Dindigul'),
    ('Dudhwa National Park', 'Dudhwa National Park'),
    ('Dwaraka', 'Dwaraka'),
    ('Ernakulam', 'Ernakulam'),
    ('Faridabad', 'Faridabad'),
    ('Gadag', 'Gadag'),
    ('Ghaziabad', 'Ghaziabad'),
    ('Gandhinagar', 'Gandhinagar'),
    ('Gangotri', 'Gangotri'),
    ('Gangtok', 'Gangtok'),
    ('Gir Wildlife Sanctuary', 'Gir Wildlife Sanctuary'),
    ('Goa', 'Goa'),
    ('Gobichettipalayam', 'Gobichettipalayam'),
    ('Great Himalayan National Park', 'Great Himalayan National Park'),
    ('Gulmarg', 'Gulmarg'),
    ('Gurgaon', 'Gurgaon'),
    ('Guruvayoor', 'Guruvayoor'),
    ('Guwahati', 'Guwahati'),
    ('Gwalior', 'Gwalior'),
    ('Hampi', 'Hampi'),
    ('Haridwar', 'Haridwar'),
    ('Hogenakkal', 'Hogenakkal'),
    ('Horsley Hills', 'Horsley Hills'),
    ('Hyderabad', 'Hyderabad'),
    ('Idukki', 'Idukki'),
    ('Imphal', 'Imphal'),
    ('Indore', 'Indore'),
    ('Itangar', 'Itangar'),
    ('Jabalpur', 'Jabalpur'),
    ('Jaipur', 'Jaipur'),
    ('Jaisalmer', 'Jaisalmer'),
    ('Jalandhar', 'Jalandhar'),
    ('Jammu', 'Jammu'),
    ('Jamshedpur', 'Jamshedpur'),
    ('Jodhpur', 'Jodhpur'),
    ('Kanchipuram', 'Kanchipuram'),
    ('Kanha National Park', 'Kanha National Park'),
    ('Kanpur', 'Kanpur'),
    ('Kanyakumari', 'Kanyakumari'),
    ('Kargil', 'Kargil'),
    ('Karunagappally', 'Karunagappally'),
    ('Karwar', 'Karwar'),
    ('Kausani', 'Kausani'),
    ('Kedarnath', 'Kedarnath'),
    ('Keoladeoghana National Park', 'Keoladeoghana National Park'),
    ('Khajuraho', 'Khajuraho'),
    ('Kochi', 'Kochi'),
    ('Kodaikanal', 'Kodaikanal'),
    ('Kolkata', 'Kolkata'),
    ('Kollam', 'Kollam'),
    ('Konark', 'Konark'),
    ('Kotagiri', 'Kotagiri'),
    ('Kottakkal and Ayurveda', 'Kottakkal and Ayurveda'),
    ('Kovalam', 'Kovalam'),
    ('Kovalam and Ayurveda', 'Kovalam and Ayurveda'),
    ('Kudremukh', 'Kudremukh'),
    ('Kullu', 'Kullu'),
    ('Kumaon', 'Kumaon'),
    ('Kumarakom', 'Kumarakom'),
    ('Kumarakom and Ayurveda', 'Kumarakom and Ayurveda'),
    ('Kumarakom Bird Sanctuary', 'Kumarakom Bird Sanctuary'),
    ('Kurukshetra', 'Kurukshetra'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Lucknow', 'Lucknow'),
    ('Ludhiana', 'Ludhiana'),
    ('Madurai', 'Madurai'),
    ('Mahabalipuram', 'Mahabalipuram'),
    ('Malpe Beach', 'Malpe Beach'),
    ('Manas National Park', 'Manas National Park'),
    ('Mangalore', 'Mangalore'),
    ('Maravanthe Beach', 'Maravanthe Beach'),
    ('Margoa', 'Margoa'),
    ('Morbi', 'Morbi'),
    ('Mount Abu', 'Mount Abu'),
    ('Mumbai', 'Mumbai'),
    ('Munnar', 'Munnar'),
    ('Mussoorie', 'Mussoorie'),
    ('Mysore', 'Mysore'),
    ('Nagpur', 'Nagpur'),
    ('Nahsik', 'Nahsik'),
    ('Nalanda', 'Nalanda'),
    ('Nanda Devi National Park', 'Nanda Devi National Park'),
    ('Nandi Hills', 'Nandi Hills'),
    ('Netravali Wild Life Sanctuary', 'Netravali Wild Life Sanctuary'),
    ('Neyveli', 'Neyveli'),
    ('Noida', 'Noida'),
    ('Ooty', 'Ooty'),
    ('Orchha', 'Orchha'),
    ('Pahalgam', 'Pahalgam'),
    ('Palakkad', 'Palakkad'),
    ('Panchgani', 'Panchgani'),
    ('Patna', 'Patna'),
    ('Patnitop', 'Patnitop'),
    ('Pattadakkal', 'Pattadakkal'),
    ('Periyar Wildlife Sanctuary', 'Periyar Wildlife Sanctuary'),
    ('Pithoragarh', 'Pithoragarh'),
    ('Pondicherry', 'Pondicherry'),
    ('Pune', 'Pune'),
    ('Puri', 'Puri'),
    ('Pushkar', 'Pushkar'),
    ('Raipur', 'Raipur'),
    ('Rajaji National Park', 'Rajaji National Park'),
    ('Rajnandgaon', 'Rajnandgaon'),
    ('Rajgir', 'Rajgir'),
    ('Rameshwaram', 'Rameshwaram'),
    ('Ranchi', 'Ranchi'),
    ('Ranganthittu Bird Sanctuary', 'Ranganthittu Bird Sanctuary'),
    ('Ranikhet', 'Ranikhet'),
    ('Ranthambore', 'Ranthambore'),
    ('Resubelpara', 'Resubelpara'),
    ('Rishikesh', 'Rishikesh'),
    ('Rourkela', 'Rourkela'),
    ('Sambalpur', 'Sambalpur'),
    ('Sanchi', 'Sanchi'),
    ('Saputara', 'Saputara'),
    ('Sariska Wildlife Sanctuary', 'Sariska Wildlife Sanctuary'),
    ('Shillong', 'Shillong'),
    ('Shimla', 'Shimla'),
    ('Sohna_Hills', 'Sohna_Hills'),
    ('Srinagar', 'Srinagar'),
    ('Sunderbans', 'Sunderbans'),
    ('Surat', 'Surat'),
    ('Tezpur', 'Tezpur'),
    ('Thanjavur', 'Thanjavur'),
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Thrissur', 'Thrissur'),
    ('Tirunelveli', 'Tirunelveli'),
    ('Tirupati', 'Tirupati'),
    ('Tiruppur', 'Tiruppur'),
    ('Trichy', 'Trichy'),
    ('Udaipur', 'Udaipur'),
    ('Udupi', 'Udupi'),
    ('Ujjain', 'Ujjain'),
    ('Vaishali', 'Vaishali'),
    ('Valley of Flowers', 'Valley of Flowers'),
    ('Varanasi', 'Varanasi'),
    ('Varkala and Ayurveda', 'Varkala and Ayurveda'),
    ('Vijayawada', 'Vijayawada'),
    ('Vishakhapatnam', 'Vishakhapatnam'),
    ('Vrindhavan', 'Vrindhavan'),
    ('Warangal', 'Warangal'),
    ('Wayanad', 'Wayanad'),
    ('Wayanad Wildlife Sanctuary', 'Wayanad Wildlife Sanctuary'),
    ('Yercaud', 'Yercaud'),
    ('Zanskar', 'Zanskar')
)


def get_default_json():
    return {}


def get_default_list():
    return []


class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True, default='')
    email = models.CharField(max_length=255, null=True, blank=True, default='')
    phone_number = models.CharField(max_length=255, null=True, blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255, null=False, blank=False, default='ACCESSORY',
                            choices=[(PRODUCT_ACCESSORY, PRODUCT_ACCESSORY), (PRODUCT_VEHICLE, PRODUCT_VEHICLE)])
    maximum_retail_price = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    model_number = models.CharField(max_length=255, null=True, blank=True, default='')
    slug = models.CharField(max_length=255, default="", unique=True)
    image_url = models.CharField(max_length=255, null=True, blank=True, default='')
    bg_image = models.CharField(max_length=255, null=True, blank=True, default='')
    title = models.CharField(max_length=255, null=True, blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)
    is_out_of_stock = models.BooleanField(default=False)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return str(self.name)


class ProductContent(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    landing_page_content = models.TextField(null=True, blank=True)
    landing_page_image = models.CharField(max_length=255, null=True, blank=True, default='')
    info_page_content_1 = models.TextField(null=True, blank=True)
    info_page_content_2 = models.TextField(null=True, blank=True)
    video_page_video_link = models.CharField(max_length=255, null=True, blank=True, default='')
    stats_page_heading = models.TextField(null=True, blank=True)
    stats_page_content = models.TextField(null=True, blank=True)
    stats_page_metrics = models.JSONField(default=get_default_json, blank=True)
    features_page_heading_1 = models.TextField(null=True, blank=True)
    features_page_heading_2 = models.TextField(null=True, blank=True)
    features_page_content_1 = models.TextField(null=True, blank=True)
    features_page_metrics_1 = ArrayField(models.CharField(max_length=255), default=get_default_list, blank=True)
    features_page_metrics_2 = ArrayField(models.CharField(max_length=255), default=get_default_list, blank=True)
    pricing_page_amount = models.CharField(max_length=255, null=True, blank=True, default='0')
    pricing_page_emi = models.CharField(max_length=255, null=True, blank=True, default='0')

    primary_color = models.CharField(max_length=255, null=True, blank=True, default='')
    info_page_bg_image_url = models.CharField(max_length=255, null=True, blank=True, default='')
    info_4_bg_image_1 = models.CharField(max_length=255, null=True, blank=True, default='')
    info_4_bg_image_2 = models.CharField(max_length=255, null=True, blank=True, default='')
    whats_more_bg_image = models.CharField(max_length=255, null=True, blank=True, default='')
    stats_bg_image = models.CharField(max_length=255, null=True, blank=True, default='')
    specification_bg = models.CharField(max_length=255, null=True, blank=True, default='')
    home_slider_bg_url = models.CharField(max_length=255, null=True, blank=True, default='')
    home_slider_title = models.CharField(max_length=255, null=True, blank=True, default='')
    whats_more_subtitle_text = models.TextField(null=True, blank=True)
    features_page_main_stat = models.JSONField(default=get_default_json, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_content'

    def __str__(self):
        return str(self.product.name)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cart'


class UserAddress(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=True, default='')
    phone_number = models.CharField(max_length=255, null=True, blank=True, default='')
    pincode = models.CharField(max_length=255, null=True, blank=True, default='')
    address_line_1 = models.CharField(max_length=255, null=True, blank=True, default='')
    address_line_2 = models.CharField(max_length=255, null=True, blank=True, default='')
    landmark = models.CharField(max_length=255, null=True, blank=True, default='')
    city = models.CharField(max_length=255, null=True, blank=True, default='')
    state = models.CharField(max_length=255, null=True, blank=True, default='')
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_address'

    def __str__(self):
        return "{}({})\n{}\n{}\n{}\n{}".format(self.full_name,
                                               self.phone_number, self.address_line_1, self.address_line_2, self.landmark,
                                               self.city, self.state, self.pincode)


class Order(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, default=ORDER_VIRTUAL)
    base_amount = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)
    gst_amount = models.IntegerField(default=0)
    discount_amount = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        super(Order, self).save(*args, **kwargs)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_item'

    def __str__(self):
        return str(self.order.id)


class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255)
    medium = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transaction'

    def __str__(self):
        return str(self.order.id + " - " + self.transaction_id)


class Warranty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    frame_number = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'warranty'

    def __str__(self):
        return str(self.frame_number)


class Lead(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, default='')
    phone = models.CharField(max_length=255, null=True, blank=True, default='')
    email = models.CharField(max_length=255, null=True, blank=True, default='')
    city = models.CharField(max_length=255, null=True, blank=True, default='')
    form_name = models.CharField(max_length=255, null=True, blank=True, default='')
    meta = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lead'

    def __str__(self):
        return str(self.name)


class InsuranceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    frame_number = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'insurance_request'

    def __str__(self):
        return str(self.frame_number)


class EmailLeadLogs(models.Model):
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    form_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    interest = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    cycle_id = models.CharField(max_length=255, blank=True, null=True)
    product_id = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    preferred_date = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'email_lead_logs'

    def __str__(self):
        return str(self.email)


class Dealer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255, default=None, null=True, choices=CITY_CHOICES)
    email = models.CharField(max_length=255, default=None, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dealer'

    def __str__(self):
        return str(self.name)


class TestRideBooking(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, null=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    is_scheduled = models.BooleanField(default=False)
    scheduled_at = models.DateTimeField(default=None, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'test_ride_booking'

    def __str__(self):
        return str(self.name)
