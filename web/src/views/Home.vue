<template>
  <div class="home">
    <div class="container">
        <div class="row">
            <div class="col align-self-center" style="width:100%; margin-top:30px">
                <Card style="width: 100%;">
                    <template #content>
                            <p>El 2 de abril de 2013, la ciudad de La Plata sufrió un evento extraordinario que provocó que
                            distintas zonas de la ciudad quedaran inundadas con graves consecuencias.</p>
                            <p>Esta aplicación nos permite conocer y gestionar zonas con peligro de inundación y las acciones a llevar a cabo en caso
                                de suceder un evento de este estilo. Por otro lado tambíen nos permite brindar información a los y las habitantes de la ciudad de La Plata.</p>                            
                    </template>
                </Card>
            </div>
        </div>
    </div>

        <div class="container"  style="margin-top:30px">
      <div class="row" >
        <div class="col" style="align-items: center">
        <Card style="width: 22.5em, align-items: center">
            <template #header>
                <img src="../assets/puntos.jpg" class="image"/>
            </template>
            <template #title>
                Ver mapa con denuncias
            </template>
            <template #content>
                <p>En esta sección se visualiza un mapa de la aplicación en el cual se muestra información referida a las denuncias en trámite.</p>
            </template>
            <template #footer>
                <router-link to="/denuncias/all">
                    <Button label="Mapa de denuncias" class="p-button-info" />
                </router-link>
             </template>
        </Card>
        </div>
        <div class="col" >
        <Card style="width: 22.5em, align-items: center">
            <template #header>
                <img src="../assets/recorridos.png" class="image"/>
            </template>
            <template #title>
                Ver recorridos de evacuación
            </template>
            <template #content>
                <p>En esta sección se visualiza un mapa de la aplicación en el cual se muestra información referida a los recorridos de evacuaciones.</p>
            </template>
            <template #footer>
                <router-link to="/recorridos_puntos">
                    <Button label="Recorridos de evacuación" class="p-button-info" />
                </router-link>
             </template>
        </Card>
        </div>

      </div>

      <div class="row justify-content-center" style="margin-top:40px; margin-bottom:40px ">
                <div class="col" >
        <Card style="width: 22.5em, align-items: center">
            <template #header>
                <img src="../assets/zonas_inundables.jpg" class="image"/>
            </template>
            <template #title>
                Ver zonas inundables
            </template>
            <template #content>
                <p>En esta sección podrá visualizar un mapa con las zonas inundables, debajo podrá ver un listado con información de cada zona.</p>
            </template>
            <template #footer>
                <router-link to="/zonas_inundables">
                    <Button label="Zonas inundables" class="p-button-info" />
                </router-link>
             </template>                         
        </Card>
        </div>
        <div class="col" >
        <Card style="width: 22.5em, align-items: center">
            <template #header>
                <img src="../assets/denuncias.jpg" class="image"/>
            </template>
            <template #title>
                Realizar denuncias 
            </template>
            <template #content>
                <p>En este apartado podrá realizar una denuncias informando el hecho y datos de contacto para un mejor servicio.</p>
            </template>
            <template #footer>
                <router-link to="/carga_denuncias">
                    <Button label="Realizar denuncia" class="p-button-info" />
                </router-link>
             </template>  
        </Card>
        </div>

    </div>
  </div>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss" scoped>
p {
    line-height: 1.5;
    margin: 0;
}

.image{
    border-radius: 70%;
    height: 15rem;
    width: 15rem;
}
</style>