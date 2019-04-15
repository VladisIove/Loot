<template>
	<div id="app">
		<v-card height="50px" flat>
			<v-bottom-nav
			:value="true"
			absolute
			color="transparent"
			>
			<v-btn
			color="teal"
			flat
			value="recent"
			>
			<span>Быстрый заказ</span>
			<v-icon>history</v-icon>
		</v-btn>

		<v-btn
		color="teal"
		flat
		value="favorites"
		>
		<span>Боксы</span>
		<v-icon>favorite</v-icon>
	</v-btn>

	<v-btn
	color="teal"
	flat
	value="nearby"
	>
	<span>Заказать онлайн</span>
	<v-icon>place</v-icon>
</v-btn>
</v-bottom-nav>
</v-card>


<v-parallax
dark
src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
>
<v-layout
align-center
column
justify-center
>
<v-form v-model="valid">
    <v-container>
      <v-layout>
        <v-flex
          xs12
          md4
        >
          <v-text-field
            v-model="firstname"
            :rules="nameRules"
            :counter="10"
            label="Введите номер телефона"
            required
          ></v-text-field>
          <v-btn @click="submit">submit</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-form>
</v-layout>
</v-parallax>
<v-layout >
	<v-flex v-for = 'loot in loots'>
		<v-card>
			<v-img
			v-bind:src="loot.img"
			aspect-ratio="2.75"
			></v-img>

			<v-card-title primary-title>
				<div>
					<h3 class="headline mb-0">{{loot.name}}</h3>
					<span class="grey--text">{{loot.price}}</span>
					<span class="grey--text">{{loot.size_loot}}</span>
					<div>{{ loot.descr }}</div>
				</div>
			</v-card-title>

			<v-card-actions>
				<v-btn flat color="orange">Заказать</v-btn>
			</v-card-actions>
		</v-card>
	</v-flex>
</v-layout>


<v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Name"
      required
    ></v-text-field>

    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field>

    <v-select
      v-model="select"
      :items="items"
      :rules="[v => !!v || 'Item is required']"
      label="Item"
      required
    ></v-select>

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must agree to continue!']"
      label="Do you agree?"
      required
    ></v-checkbox>

    <v-btn
      :disabled="!valid"
      color="success"
      @click="validate"
    >
      Validate
    </v-btn>

  
  </v-form>


<v-footer dark height="auto" >
	<v-card
	class="flex"
	flat
	tile
	>
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
</div>
</template>

<script>
	

	export default {
		name: 'Loot',

		data () {
			return {
				loots: '',
				valid: true,
				name: '',
				nameRules: [
				v => !!v || 'Name is required',
				v => (v && v.length <= 10) || 'Name must be less than 10 characters'
				],
				email: '',
				emailRules: [
				v => !!v || 'E-mail is required',
				v => /.+@.+/.test(v) || 'E-mail must be valid'
				],
				select: null,
				items: [
				'Item 1',
				'Item 2',
				'Item 3',
				'Item 4'
				],
				checkbox: false
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
						this.loots = response.data
						console.log(this.loots)
					}
				})
			},
			validate () {
				if (this.$refs.form.validate()) {
					this.snackbar = true
				}
			},
		}

	}
</script>

<style lang="css" scoped>
</style>