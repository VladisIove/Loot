<template>
	<v-app>
		<v-card height="50px" flat>
			<v-bottom-nav :value="true"	absolute color="transparent">
				
				<v-btn	color="teal" flat value="recent" href="#head1" >
					
						<span>Быстрый заказ</span>
						<v-icon>history</v-icon>
	
				</v-btn>
				
				
				<v-btn	color="teal" flat value="favorites" href="#head2" >
						<span>Боксы</span>
						<v-icon>favorite</v-icon>
				</v-btn>


				<v-btn color="teal" flat value="nearby" href="#head3" >

						<span>Заказать онлайн</span>
						<v-icon>place</v-icon>
			
				</v-btn>

			</v-bottom-nav>
		</v-card>



		<div class="" id="head1">
			<Paralax ></Paralax>
		</div>
		<div class="" id="head2">
			<Main ></Main>
		</div>
		<div class="" id="head3">
			<Order></Order> 
		</div>
		<v-footer dark height="auto" >
			<v-card	class="flex" flat tile>
				<v-card-title class="teal">
					<strong class="subheading">Slogan companies!</strong>
					<v-spacer></v-spacer>
					<strong class="subheading">E-mail: vvvvv@gmail.com</strong>
				</v-card-title>
				<v-card-actions class="grey darken-3 justify-center">
					&copy;2018 — <strong>Vuetify</strong>
				</v-card-actions>
			</v-card>
		</v-footer>
	</v-app>
</template>

<script>



import Paralax from './include/paralax.vue'
import Main from './include/main.vue'
import Order from './include/order.vue'

export default {
	name: 'Loot',

	data () {
		return {

		}
	},
	components: {
		Paralax,
		Main,
		Order
	},
	methods: {
	}
}

</script>

<style scoped lang="sass">

</style>