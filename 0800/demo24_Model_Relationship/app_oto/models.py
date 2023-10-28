from django.db import models
# from django.contrib.auth.models import User


# One to Many
# =====================================================
# class Course(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     course_name = models.CharField(max_length=60)
#     duration = models.IntegerField()

# PROTECTED
# class Course(models.Model):
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     course_name = models.CharField(max_length=60)
#     duration = models.IntegerField()


# SET NULL
# class Course(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     course_name = models.CharField(max_length=60)
#     duration = models.IntegerField()

# Set Default
# ----------------------------
# class Category(models.Model):
#     cat_name = models.CharField(max_length=60)
#
#     def __str__(self):
#         return self.cat_name


# class Product(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=6)
#     product_name = models.CharField(max_length=60)
#     price = models.IntegerField()


# Saurav - Phone - Iphone 15 pro utra
# Saurav - Phone - Samsung s3
# Saurav - Cloths - Jacket

# Ankit - Furniture - Sofa Set





# Create your models here.

# 1 will create a separate column for foreign key/ connectivity
# class StudentDetail(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     age = models.IntegerField()
#     city = models.CharField(max_length=50)


# 2will not create a separate column for foreign key/ connectivity
# class StudentDetail(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     age = models.IntegerField()
#     city = models.CharField(max_length=50)


# 3will not create a separate column for foreign key/ connectivity
# class StudentProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     age = models.IntegerField()
#     city = models.CharField(max_length=50)
#
#
# class StudentMarksheet(StudentProfile):
#     maths = models.IntegerField()
#     science = models.IntegerField()
#     english = models.IntegerField()
#     skt = models.IntegerField()
#     total = models.IntegerField()
#     average = models.IntegerField()


# 4 Way
# class StudentDetail(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     age = models.IntegerField()
#     city = models.CharField(max_length=50)
#
#
# class StudentMarksheet(models.Model):
#     student_detail = models.OneToOneField(StudentDetail, on_delete=models.CASCADE)
#     maths = models.IntegerField()
#     science = models.IntegerField()
#     english = models.IntegerField()
#     skt = models.IntegerField()
#     total = models.IntegerField()
#     average = models.IntegerField()


class Teacher(models.Model):
    t_name = models.CharField(max_length=60)
    quali = models.CharField(max_length=60)
    salary = models.IntegerField()

    def __str__(self):
        return self.t_name


class Student(models.Model):
    teacher = models.ManyToManyField(Teacher)
    s_name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    age = models.CharField(max_length=60)

