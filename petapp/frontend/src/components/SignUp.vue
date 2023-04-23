<template>
    <div v-html="signup"></div>
</template>
  
<script>
    import DjangoRender from 'site-packages.django_render';

    export default {
        data(){
            return{
                signup: '',
            };
        },

        async created(){
            const response=await fetch('signup');
            const data=await response.text();
            this.signup=DjangoRender.parse(data).html;
        },

    };
</script>
