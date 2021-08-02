from django.db import models

class ModeloBaseMaster(models.Model):
    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True, null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True, null=True)
    pcid = models.CharField(max_length=200, blank=True, null=True, editable=False)
    estado = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        try:
            user = args[0].user
        except:
            user = None
        try:
            if self._state.adding:
                self.creadopor = user.username if user is not None else 'Admin'
            else:
                self.editadopor = user.username if user is not None else 'Admin'
        except:
            pass
        models.Model.save(self)

    class Meta:
        abstract = True


class Empresa(ModeloBaseMaster):
    codigo = models.CharField(max_length=10,blank=True,null=True,verbose_name='Código')
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10,choices=(('PRIVADA','Privada'),('PUBLICA','Publica')),blank=True,null=True)
    ciudad = models.CharField(max_length=100,blank=True,null=True)
    representante = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['-creadodate']
