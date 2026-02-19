from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Nome", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['name']


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model=models.CharField("Modelo", max_length=100)
    
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name="Marca",related_name="car_brand")
    
    factory_year = models.IntegerField("Ano de Fabricação", blank=True, null=True)
    model_year = models.IntegerField("Ano de Modelo", blank=True, null=True)
    plate = models.CharField("Placa", max_length=20, blank=True, null=True)
    value=models.DecimalField("Valor", max_digits=10, decimal_places=2, blank=True, null=True)
    photo = models.ImageField("Foto", upload_to='cars/', blank=True, null=True)
    bio = models.TextField("Descrição", blank=True, null=True)

    def __str__(self):
        return self.model
    
    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"
        ordering = ['model']
    

class CarInventory(models.Model):
   cars_count=models.IntegerField("Quantidade de Carros")
   cars_value=models.DecimalField("Valor Total dos Carros", max_digits=15, decimal_places=2)
   created_at=models.DateTimeField("Criado em", auto_now_add=True)
   
   
   def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'

   
   class Meta:
       ordering = ['-created_at']
       verbose_name = "Inventário de Carros"
       verbose_name_plural = "Inventários de Carros"