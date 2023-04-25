<template>
        <!-- LOGO -->
        <div>
            <img loading="auto" src="/media/oscar6.png" width="200">
        </div>

        <!-- TITLE -->
        <div class="text-info">
            <h1>HOME PAGE</h1>
        </div>

        <!-- SIGN UP/ LOG IN -->


        <!-- BUTTON FOR DOG MAP -->
        <div>
            <div class="tab-buttons">
                <router-link to="/">SignUp</router-link>
                <router-link to="/dogs-map">DogsMap</router-link>
                <router-link to="/log-in">LogIn</router-link>
            </div>
            <router-view></router-view>

        </div>
</template>

<script>
    import DogsMap from '../components/DogsMap.vue'
    import SignUp from '../components/SignUp.vue'
    import LogIn from '../components/LogIn.vue'

    export default{
        components:{
            DogsMap,
            SignUp,
            LogIn
        },

        data(){
            return{
                currentComponent:  'Index',

                tabs: [
                    {name: 'SignUp', component: 'SignUp'},
                    {name: 'DogsMap', component: 'DogsMap'},
                    {name: 'LogIn', component: 'LogIn'}
                ]
            }
        },

        methods:{
            changeTab(tabName) {
                this.$router.push('/' + tabName.toLowerCase())
            }
        }
    }

</script>