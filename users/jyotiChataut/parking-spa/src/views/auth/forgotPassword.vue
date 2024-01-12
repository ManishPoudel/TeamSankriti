<template>
  <div class="flex items-center justify-center">
    <div class="w-1/2">
      <div
        class="relative flex-col item-end min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0"
      >
        <form @submit.prevent="submit">
          <label for="email">email</label>
          <input v-model="email" type="text" name="email" placeholder="Enter your email here..."/>
          <div>
            <button type="submit" @click="forgotPassword()">Submit</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
export default {
    data(){
        return{
            email:null
        }
    },
    methods:{
        forgotPassword(){
            console.log('Jyoti')
        }
    }
}
</script>