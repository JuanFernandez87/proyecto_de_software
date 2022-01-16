from wtforms import Form, StringField, validators, ValidationError, SelectField, IntegerField
from wtforms.fields.simple import HiddenField
from datetime import date, timedelta

estados = ["Todos", "Sin confirmar", "En curso", "Resuelta", "Cerrada"] 
categorias = [('1', 'Basural'), ('2', 'Alcantarilla tapada')]

class UpdateForm(Form):    
    def length(min=1, max=30):
        message = 'Debe tener entre %d y %d caracteres' % (min, max)

        def _length(form, field):
            l = field.data and len(field.data) or 0
            if l < min or max != -1 and l > max:
                raise ValidationError(message)

        return _length
    estados = ["Sin confirmar", "En curso", "Resuelta"]
    id = HiddenField('')
    titulo = StringField('Titulo', [validators.DataRequired("Campo requerido"), length(max=25)])
    categoria = SelectField('Categoria', [validators.DataRequired("Campo requerido")], choices=categorias)
    fecha_creacion = StringField('Fecha de creación', render_kw = {'readonly': True})
    descripcion = StringField('Descripción', [validators.DataRequired("Campo requerido"), length(max=30)])
    latitud = StringField('lat', render_kw = {'readonly': True})
    longitud = StringField('lng', render_kw = {'readonly': True})
    estado = SelectField('Estado', [validators.DataRequired("Campo requerido")], choices=estados)
    apellido_denunciante = StringField('Apellido', [validators.DataRequired("Campo requerido"), length(max=25)])
    nombre_denunciante = StringField('Nombre', [validators.DataRequired("Campo requerido"), length(max=25)])
    intentos_comunicacion = IntegerField('Cantidad de intentos de comunicación' , [validators.NumberRange(min=0, max=3, message='La cantidad de intentos no debe ser mayor a 3')])
    tel_cel_denunciante = StringField('Telefono/Celular', [validators.DataRequired("Campo requerido"), length(max=25)])
    email_denunciante = StringField('Email', [validators.DataRequired("Campo requerido"), validators.Email("Formato de email inválido.")])

class RegistrationFormCreate(Form):
    def length(min=1, max=30):
        message = 'Debe tener entre %d y %d caracteres' % (min, max)

        def _length(form, field):
            l = field.data and len(field.data) or 0
            if l < min or max != -1 and l > max:
                raise ValidationError(message)

        return _length
    id = HiddenField('')
    titulo = StringField('Titulo', [validators.DataRequired("Campo requerido"), length(max=25)])
    categoria = SelectField('Categoria', [validators.DataRequired("Campo requerido")], choices=[('0', 'Basural'), ('1', 'Alcantarilla tapada')])
    descripcion = StringField('Descripción', [validators.DataRequired("Campo requerido"), length(max=30)])
    latitud = StringField('lat', render_kw = {'readonly': True})
    longitud = StringField('lng', render_kw = {'readonly': True})
    apellido_denunciante = StringField('Apellido', [validators.DataRequired("Campo requerido"), length(max=25)])
    nombre_denunciante = StringField('Nombre', [validators.DataRequired("Campo requerido"), length(max=25)])
    tel_cel_denunciante = StringField('Telefono/Celular', [validators.DataRequired("Campo requerido"), length(max=25)])
    email_denunciante = StringField('Email', [validators.DataRequired("Campo requerido"), validators.Email("Formato de email inválido.")])

class FormFiltro(Form):
    def validador_fecha(form, field):
        if form.fecha_inicio.data > field.data:
            raise ValidationError('La fecha desde debe ser menor que la fecha hasta')

    estado = SelectField('Filtrar por estado', choices=estados)
    titulo = StringField('Filtrar por titulo')
    fecha_inicio = StringField('Fecha desde:') 
    fecha_fin = StringField('Fecha hasta:', [validador_fecha])
