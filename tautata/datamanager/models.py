from django.db import models


class Farmers(models.model):
    farmer_id = models.IntegerField(default=0)
    farmer_name = models.charfield(max_length=250)
    village_name = models.ForeignKey(Districts,default=None)
    lrp_id = models.ForeignKey(LRPs,default=None)
    last_date_of_survey = models.DateTimeField('date published')
    farmer_latitude_gps = models.floatField(default=0)
    farmer_longitude_gps = mmodels.floatField(default=0)
    farmer_altitude = models.floatField(default=0)

class Districts(models.model):#is the name of the table Villages or Districts?
    village_name = models.charfield(max_length=250)
    district_name = models.charfield(max_length=250)

class LRPs(models.model):
    lrp_id = models.charfield(max_length=250)
    lrp_name = models.charfield(max_length=250)
    village_name = models.ForeignKey(Districts,default=None)
    lrp_phone_num = models.IntegerField(default=0)
    lrp_traning_date = models.DateTimeField('date published')

class Substances(models.model):
    sub_name = models.charfield(max_length=250)
    sub_kind = models.charfield(max_length=250)
    sub_type = models.charfield(max_length=250)
    sub_mu = models.charfield(max_length=250)

class Obs_Sub_Used(models.model):
    obs_id = models.IntegerField(default=0)
    sub_name = models.charfield(max_length=250)
    sub_u_days = models.charfield(max_length=250)
    sub_u_amount = models.floatField(default=0)
 
class Obs_Sub_Bought(models.model):
    obs_id = models.IntegerField(default=0)
    sub_name = models.charfield(max_length=250)
    sub_b_amount = models.floatField(default=0)
    sub_b_cost = models.floatField(default=0)

class Obs_Damages(models.model):
    obs_id= models.IntegerField(default=0)
    damage_name = models.charfield(max_length=250)
    damage_type = models.charfield(max_length=250)
    damage_treat = models.charfield(max_length=250)
    damage_pic = models.charfield(max_length=250)

class Obs_Expenses(models.model):
    obs_id =  models.IntegerField(default=0)
    exp_name = models.charfield(max_length=250)
    exp_type = models.charfield(max_length=250)
    exp_cost = models.floatField(default=0)

class Observations(models.model):
    obs_id = models.IntegerField(default=0)
    obs_date  = models.DateTimeField('date published')
    obs_time = models.TimeField('date published')
    lrp_id = models.ForeignKey(LRPs,default=None)
    farmer_id = models.ForeignKey(Farmers,default=None)
    obs_latitude_gps = models.floatField(default=0)
    obs_longitude_gps = models.floatField(default=0)
    obs_altitude_gps = models.floatField(default=0)
    obs_crop = models.charfield(max_length=250)
    drips_bool = models.booleanfield()
    irri_days = models.charfield(max_length=250)
    irri_hours = models.floatField(default=0)
    water_cost = models.floatField(default=0)
    irri_cost = models.floatField(default=0)
    work_in_plot = models.charfield(max_length=250)
    lab_farmer_days = models.IntegerField(default=0)
    lab_farmer_hours = models.floatField(default=0)
    lab_spouce_days = models.IntegerField(default=0)
    lab_spouce_hours = models.floatField(default=0)
    lab_oth_hh_num =  models.IntegerField(default=0)     #mistake in the excel file, twice b_oth_hh_days fields
    lab_oth_hh_days = models.floatField(default=0) 
    plab_num = models.IntegerField(default=0)
    plab_days = models.IntegerField(default=0)
    plab_tot_cost = models.floatField(default=0)
    harvest_kg = models.floatField(default=0)
    storge_kg = models.floatField(default=0)
    damage_kg = models.floatField(default=0)
    sold_bool = models.booleanfield()
    sold_to = models.charfield(max_length=250)
    sold_kg = models.floatField(default=0)
    one_price_bool = models.booleanfield()
    one_price = models.floatField(default=0)
    dif_price_reason = models.charfield(max_length=250)
    high_price = models.floatField(default=0)
    high_price_kg = models.floatField(default=0)
    low_price = models.floatField(default=0)
    low_price_kg = models.floatField(default=0)
    tot_revenue = models.floatField(default=0)
    plant_hight = models.floatField(default=0)
    plant_pic = models.charfield(max_length=250)
    veg_pic = models.charfield(max_length=250)
    leaf_pic = models.charfield(max_length=250)
    plot_pic = models.charfield(max_length=250)
    obs_notes = models.charfield(max_length=250)
    
