from django.db import models


class Business(models.Model):
    class Meta:
        verbose_name = "Business"
        verbose_name_plural = "Businesses"
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=20, unique=True, default="")
    country_code = models.CharField(max_length=20, default="EU")

    def __str__(self):
        return self.name
    

class QuarterReport(models.Model):
    class Meta:
        verbose_name = "Quarter Report"
        verbose_name_plural = "Quarter Reports"
    business = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)
    year = models.IntegerField(default=1970)
    quarter = models.IntegerField(default=1)
    earning = models.IntegerField()
    revenue = models.IntegerField()

    def __str__(self):
        return f"{self.business}_{self.year}Q{self.quarter}"


class YearlyReport(models.Model):
    class Meta:
        verbose_name = "Yearly Report"
        verbose_name_plural = "Yearly Reports"
    business = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)
    year = models.IntegerField(default=1970)
    earning = models.IntegerField()
    revenue = models.IntegerField()

    def __str__(self):
        return f"{self.business}_{self.year}"