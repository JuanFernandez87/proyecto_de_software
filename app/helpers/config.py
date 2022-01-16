def get_color_header(session):
    if(session.get("color_header")):
        return session.get("color_header")
    return "#FFFFFF"
def get_color_footer(session):
    if(session.get("color_footer")):
        return session.get("color_footer")
    return "#212121"

def get_color_boton(session):
    if(session.get("color_boton")):
        return session.get("color_boton")   
    return "#008290" 