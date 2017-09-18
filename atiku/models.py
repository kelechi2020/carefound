from django.db import models


STATE_CHOICE = (('ABIA', 'ABIA'), ('ADAMAWA', 'ADAMAWA'), ('AKWAIBOM', 'AKWAIBOM'), ('ANAMBRA', 'ANAMBRA'),
          ('BAUCHI', 'BAUCHI'), ('BAYELSA', 'BAYELSA'), ('BENUE', 'BENUE'), ('BORNO', 'BORNO'),
          ('CrossRivers', 'CrossRivers'), ('Delta','Delta'), ('Ebonyi','Ebonyi'), ('Edo','Edo'),
          ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'),
          ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'),
          ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'),
          ('Ondo', 'Ondo'), ('Osun', 'Osun' ), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'),
          ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')
)
# Create your models here.

SEX_CHOICE = (
        ('MALE', "MALE"),
        ('FEMALE', "FEMALE"),
    )


class ApplicantInfo (models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=40)
    last_name = models.CharField(verbose_name='Surname', max_length=40)
    mothers_maiden_name = models.CharField(verbose_name='Mothers Maiden Name', blank=True, max_length=40)
    address = models.CharField(verbose_name='Address', max_length=100)
    state = models.CharField(verbose_name='State', max_length=100, choices=STATE_CHOICE)
    local_government = models.CharField(verbose_name='Local Government', max_length=70)
    sex = models.CharField(verbose_name="Sex",max_length=10, choices=SEX_CHOICE)
    district = models.CharField(verbose_name='District', blank=True, max_length=600)
    landmark_identity = models.CharField(verbose_name='Landmark', max_length=400, blank=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=30)
    email = models.EmailField(verbose_name='E-mail', max_length=100)
    communication_means1 = models.NullBooleanField(verbose_name='Ist Means Of Communication')
    communication_means2 = models.NullBooleanField(verbose_name='Second Means Of Communication')

    def __str__(self):
        return self.first_name + '  ' + self.last_name + '   '  + 'From ' + self.state + '  ' + 'State' + '  ' + self.local_government

class LocalGovernment(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey("State")

    def __str__(self):
        return u'%s' % self.name


class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return u'%s' % self.name