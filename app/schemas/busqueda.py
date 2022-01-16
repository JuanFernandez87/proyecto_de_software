from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import query


class Busqueda(object):

    @classmethod
    def paginar_clase(cls,clase, page: int, per_page: int, orden: str = "asc") -> BaseQuery.paginate:
        # Ver lo del orden
        """Pagina una query con los siguientes parametros

        Args:
            busqueda (query): [description]
            page (int): [description]
            per_page (int): [description]
            orden (str, optional): [description]. Defaults to "asc".

        Returns:
            BaseQuery.paginate: [description]
        """
        return clase.query.paginate(page=page, per_page=per_page, error_out=False)
    @classmethod
    def procesar_busqueda(cls,tabla,page: int, per_page: int, orden: str, busco_por: str, busco_estado: str) -> BaseQuery.paginate:
        # Puedo agregar valores por defecto ?
        """Mediante algunos parametros de busqueda, genera una consulta paginada lista para mandarla a la vista

        Args:
            page (int): [description]
            per_page (int): [description]
            orden (str): [description]
            busco_por (str): [description]
            busco_estado (str): [description]

        Returns:
            BaseQuery.paginate:  tip: con .items obtengo los datos 
        """
        
        busqueda_por_valor = tabla.buscar_por_valor(busco_por)
        busqueda_por_tipo = tabla.buscar_por_tipo(busco_estado)

        resultado = BaseQuery.intersect(busqueda_por_valor, busqueda_por_tipo)

        resultado_paginado = cls._paginar(resultado, page, per_page, orden)

        return resultado_paginado
    @classmethod
    def _paginar(cls,busqueda: query, page: int, per_page: int, orden: str = "asc") -> BaseQuery.paginate:
        # Ver lo del orden
        """Pagina una query con los siguientes parametros

        Args:
            busqueda (query): [description]
            page (int): [description]
            per_page (int): [description]
            orden (str, optional): [description]. Defaults to "asc".

        Returns:
            BaseQuery.paginate: [description]
        """
        return busqueda.paginate(page=page, per_page=per_page, error_out=False)