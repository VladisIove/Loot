<template>
	<v-layout>
		<v-flex xs12 sm12>
			<v-card>
				<v-container v-bind="{ [`grid-list-${24}`]: true }" fluid>
					<v-layout row wrap align-start justify-space-between>
						<v-flex v-for="loot in loots" :key="loot.id" md3 xs12 offset-md1 id="menu">
							<v-card flat tile>
									<v-img
									:src="loot.img"
									aspect-ratio="1.75"
									></v-img>

									<v-card-title primary-title>
										<div>
											<h3 class="headline mb-0">{{loot.name}}</h3>
											<h4 class="headline mb-0">{{loot.size_loot}}</h4>
											<h4 class="headline mb-0">{{loot.price}}</h4>
											<div> {{loot.descr}} </div>
										</div>
									</v-card-title>

									<v-card-actions>
										<v-btn flat color="orange">Заказать</v-btn>
									</v-card-actions>
							</v-card>
						</v-flex>
					</v-layout>
				</v-container>
			</v-card>
		</v-flex>
	</v-layout>
</template>

<script>
	export default {

		name: 'main',

		data () {
			return {
				loots: '',
			}
		},

		created(){
			this.loadLoot()
		},
		methods: {
			loadLoot(){
				$.ajax({
					url: "http://127.0.0.1:8000/loots/",
					type: "GET",
					success: (response) => {
						this.loots = response.data.data
						console.log(this.loots)
					}
				})
			},
		}
	}
</script>

<style lang="css" scoped>
</style>