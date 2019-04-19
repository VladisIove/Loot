<template>
   <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-container>
      <v-layout>
        <v-flex xs12  md5 >
          <v-text-field
          v-model="firstname"
          :rules="nameRules"
          :counter="30"
          label="Имя"
          required
          ></v-text-field>
        </v-flex>
        <v-spacer></v-spacer>
        <v-flex
        xs12
        md5
        >
        <v-text-field
        v-model="lastname"
        :rules="nameRules"
        :counter="30"
        label="Фамилия"
        required
        ></v-text-field>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex
      xs12
      md5
      >
      <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
      ></v-text-field>
    </v-flex>
    <v-spacer></v-spacer>
    <v-flex
    xs12
    md5
    >
    <v-text-field
    v-model="phone"
    :rules="nameRules"
    :counter="30"
    label="Введите номер телефона"
    required
    ></v-text-field>
  </v-flex>


</v-layout>
<v-layout>
  <v-select
  v-model="select"
  :items="items"
  label="Item"
  required
  ></v-select>
</v-select> 
</v-layout>


<v-layout>
  <v-checkbox
  v-model="checkbox"
  :rules="[v => !!v || 'Вы должны согласиться, что бы продолжить!']"
  label="Вы согласны на обработку персональных данных?"
  required
  ></v-checkbox>
  <v-spacer></v-spacer>
  <v-btn
  :disabled="!valid"
  color="primary"
  @click="order"
  >
  Validate
</v-btn>
</v-layout>
</v-container>

</v-form>
</template>

<script>
  export default {

    name: 'order',

    data () {
      return {
       valid: false,
       firstname: '',
       lastname: '',
       phone: '',
       nameRules: [
       v => !!v || 'Это поле обязательно',
       ],
       email: '',
       emailRules: [
       v => !!v || 'E-mail обязателен',
       v => /.+@.+/.test(v) || 'E-mail должо быть валидно'
       ],
       select: null,
       items: [],
       checkbox: false
     }
   },
   created(){
     this.loadLoot()
   },
   methods: {
    validate () {
      if (this.$refs.form.validate()) {
        this.snackbar = true
      }
    },
    loadLoot(){
     $.ajax({
      url: "http://127.0.0.1:8000/loots/",
      type: "GET",
      success: (response) => {
        this.loots = response.data.data
        for(var key in this.loots){
         this.items.push(this.loots[key].name)
       }
     }
   })
   },
   order(){
     $.ajax({
      url: 'http://127.0.0.1:8000/order/',
      type: "POST",
      data: {
       f_name: this.firstname,
       s_name: this.lastname,
       phone: this.phone,
       e_mail: this.email,
       choose: this.select,
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