<template>
	<header class="header">
		<Menubar :model="items">
			<template #start>
				<img alt="logo" src="../assets/muni4.svg" height="80" class="p-mr-2">
			</template>
		</Menubar>
	</header>

	<router-view/>

	<footer class="footer">

	</footer>

</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.header {
    margin-top: 0;
	width:100%; 
    height: 92px;
	background: #FFFFFF;
    border-bottom: 1px solid #000000;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 1);
}

/*---------- FOOTER ----------*/

.row{
	display: flex;
	flex-wrap: wrap;
    justify-content: center;
}
ul{
	list-style: none;
}
.footer{
	background: #2c3e50;
    padding: 70px 0;
    bottom: 0;
    left: 0;
    width: 100%;
	border-top: 4px solid white;
	box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

/*responsive*/
@media(max-width: 767px){
  .footer-col{
    width: 50%;
    margin-bottom: 30px;
}
}
@media(max-width: 574px){
  .footer-col{
    width: 100%;
}
}
</style>

<script>
		export default {
			data() {
				return {
					items: [
						{
							label:'Home',
							icon:'pi pi-fw pi-home',
							to: "/",						
						},
						{
							label:'Recorridos y Puntos',
							icon:'pi pi-fw pi-map',
							to: "/recorridos_puntos"
						},
						{
							label:'Zonas inundables',
							icon:'pi pi-fw pi-align-center',
							to: "/zonas_inundables"
						},
						{
							label:'Mapa de denuncias',
							icon:'pi pi-fw pi-map-marker',
							to: "/denuncias/all"
						},						
						{
							label:'Realizar denuncia',
							icon:'pi pi-fw pi-book',
							to: "/carga_denuncias"
						}																	
					]
				}
			}
		}
		</script>