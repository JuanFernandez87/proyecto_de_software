from app.models.recorrido import Recorrido
from app.models.user import User
from app.models.rol import Rol
from app.models.permission import Permission
from app.models.puntos_de_encuentro import Puntos
from app.models.config_sistema import Config_sistema
from app.models.denuncia import Denuncia
from app.models.coordenada import Coordenada
import app.helpers.Permisos as Permisos
from app.models.categoria import Categoria

from datetime import date


def loadValues(db):

    # coordenadas
    coordenada_1 = Coordenada(-34.9214, -57.9544)
    coordenada_2 = Coordenada(-34.7214, -57.1544)
    coordenada_3 = Coordenada(-34.8214, -57.5544)

    # recorridos
    recorrido_1 = Recorrido('Recorrido los lagos', 'Es bastante largo', False)
    # Puntos de encuentro
    punto_1 = Puntos('punto1', '13 y 32', True, '451515', 'punto2@punto')

    # Relacion 1 a 1 Punto - coordenada
    coordenada_1.punto.append(punto_1)

    # recorrido_coordenda
    recorrido_1.recorrido.append(coordenada_1)
    recorrido_1.recorrido.append(coordenada_2)
    recorrido_1.recorrido.append(coordenada_3)

    # permisos
    permission_1 = Permission(Permisos.USUARIO_INDEX)
    permission_2 = Permission(Permisos.USUARIO_NEW)
    permission_3 = Permission(Permisos.USUARIO_DESTROY)
    permission_4 = Permission(Permisos.USUARIO_UPDATE)
    permission_5 = Permission(Permisos.USUARIO_SHOW)
    
    permission_6 = Permission(Permisos.PUNTO_INDEX)
    permission_7 = Permission(Permisos.PUNTO_NEW)
    permission_8 = Permission(Permisos.PUNTO_DESTROY)
    permission_9 = Permission(Permisos.PUNTO_UPDATE)
    permission_10 = Permission(Permisos.PUNTO_SHOW)
    
    permission_11 = Permission(Permisos.DENUNCIA_UPDATE)
    permission_12 = Permission(Permisos.DENUNCIA_DESTROY)

    permission_13 = Permission(Permisos.ZONAS_INDEX)
    permission_14 = Permission(Permisos.ZONAS_DESTROY)
    permission_15 = Permission(Permisos.ZONAS_NEW)
    permission_16 = Permission(Permisos.ZONAS_SHOW)
    permission_17 = Permission(Permisos.ZONAS_UPDATE)
    permission_13 = Permission(Permisos.ZONAS_INDEX)
    permission_14 = Permission(Permisos.ZONAS_DESTROY)
    permission_15 = Permission(Permisos.ZONAS_NEW)
    permission_16 = Permission(Permisos.ZONAS_SHOW)
    permission_17 = Permission(Permisos.ZONAS_UPDATE)

    permission_18 = Permission(Permisos.RECORRIDOS_INDEX)
    permission_19 = Permission(Permisos.RECORRIDOS_NEW)
    permission_20 = Permission(Permisos.RECORRIDOS_DESTROY)
    permission_21 = Permission(Permisos.RECORRIDOS_UPDATE)
    permission_22 = Permission(Permisos.RECORRIDOS_SHOW)

    # roles
    rol_admin = Rol("administrador")
    rol_operador = Rol("operador")

    # roles_permiso
    rol_admin.permissions.extend([permission_1, permission_2, permission_3, permission_4, permission_5,
                                 permission_6, permission_7, permission_8, permission_9, permission_10, permission_11, permission_12, permission_13, permission_14, permission_15, permission_16, permission_17,permission_18,permission_19
                                 ,permission_20,permission_21,permission_22])
    rol_operador.permissions.extend(
        [permission_1, permission_6, permission_7, permission_9, permission_10, permission_11, permission_13, permission_15, permission_16, permission_17,
        permission_18,permission_19,permission_21,permission_22])

    # usuarios
    user_0 = User('admin', 'admin', 'admin@admin.com', '123123', 'admin', 1)
    user_1 = User('admin1', 'admin1', 'admin1@admin.com', '123123', 'admin1', 1)
    user_2 = User('admin2', 'admin2', 'admin2@admin.com', '123123', 'admin2', 0)
    user_3 = User('admin3', 'admin3', 'admin3@admin.com', '123123', 'admin3', 1)
    user_4 = User('admin4', 'admin4', 'admin4@admin.com', '123123', 'admin4', 0)

    # usuario_rol
    user_0.roles.append(rol_admin)
    user_1.roles.append(rol_admin)
    user_2.roles.append(rol_operador)
    user_3.roles.append(rol_operador)
    user_4.roles.append(rol_admin)

    # configuraciones del sistema
    config_0 = Config_sistema(1, 10, '#FFFFFF', '#212121', '#008290')
    config_1 = Config_sistema(1, 10, '#FFFFFF', '#212121', '#008290')

    # denuncias
    denuncia1 = Denuncia("Reclamo", 0, "2021-10-06", "mucha basura", "-34.92539", "-57.94978", "En curso", "perez", "jose", "2215985454", 2, "jose@gmail.com")
    denuncia2 = Denuncia("Denuncia", 1, "2021-10-10", "alcantarilla tapada", "-34.92539", "-57.94978", "Sin confirmar", "lopez", "jose", "2215689562", 0, "carlos@gmail.com")
    denuncia3 = Denuncia("Reclamo", 0, "2021-10-16", "Mugre acumulada", "-34.92539", "-57.94978", "Resuelta", "perez", "jose", "2215962578", 2, "juan@gmail.com")
    denuncia4 = Denuncia("Reclamo", 1, "2021-11-02", "Mugre acumulada", "-34.92539", "-57.94978",  "Resuelta", "perez", "jose", "2215989565", 2, "josesito@gmail.com")
    denuncia5 = Denuncia("Denuncia", 0, "2021-11-04", "Mugre acumulada", "-34.92539", "-57.94978", "Sin confirmar", "perez", "jose", "2215985956", 0, "marcos@gmail.com")
    denuncia6 = Denuncia("Denuncia", 1, "2021-11-06", "Mugre acumulada", "-34.92539", "-57.94978",  "En curso", "romero", "jose", "2215658951", 1, "pedro@gmail.com")

    # usuario_denuncias
    user_0.denuncias.append(denuncia1)
    user_0.denuncias.append(denuncia2)
    user_1.denuncias.append(denuncia3)
    user_1.denuncias.append(denuncia4)
    user_2.denuncias.append(denuncia5)
    user_3.denuncias.append(denuncia6)

    # categorias
    categoria1 = Categoria("Basural")
    categoria2 = Categoria("Alcantarilla tapada")

    db.session.add_all([recorrido_1,coordenada_1,user_0, user_1, user_2, user_3, user_4, punto_1, rol_admin, rol_operador, permission_1, permission_2, permission_3, permission_4, permission_5,
                       permission_6, permission_7, permission_8, permission_9, permission_10, permission_11, permission_12,permission_13,permission_14
                       ,permission_15,permission_16,permission_17,permission_18,permission_19,permission_20,permission_21,permission_22, config_0, config_1, denuncia1, denuncia2, denuncia3, denuncia4, denuncia5, denuncia6, categoria1, categoria2])
    db.session.commit()
