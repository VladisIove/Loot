<template>
	<v-parallax dark src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg" >

		<v-layout align-center column justify-center  >

				<v-form  ref="form"    v-model="valid"    lazy-validation  >
    					<v-text-field v-model="phone"  :counter="13"  :rules="phoneRules" label="Номер телефона" required  ></v-text-field>
					<v-checkbox   v-model="checkbox" :rules="[v => !!v || 'Вы должны согласиться, что бы продолжить!']" label="Вы согласны на обработку персональных данных?" required ></v-checkbox>
					<v-btn :disabled="!valid" color="primary"  @click="order"> Отправить  </v-btn>
        </v-form>

		</v-layout>

	</v-parallax>
</template>

<script>
export default {

  name: 'Paralax',

  data () {
    return {
    	valid: true,
      phone: '',
      phoneRules: [
        v => !!v || 'Номер телефона обязателен',
      ],
      checkbox: false
    }
  },
  methods: {
      validate () {
       if (this.$refs.form.validate()) {
          this.snackbar = true
        }      		
       },
       order(){
       	$.ajax({
       		url: 'http://127.0.0.1:5000/fastorder/',
       		type: "POST",
       		data: {
       			phone: this.phone,
       		},
       		success: (response) => {
       			alert("Мы с вами свяжемся в ближайшее время")
       		}
       	})
       }
    }
}


</script>

<style lang="css" scoped>
</style>