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
                <button v-for="(tab, index) in tabs" :key="index" @click="changeTab(tab.name)">
                    {{ tab.name }}
                </button>
            </div>

            <component v-if="currentComponent === 'SignUp'" is="SignUp"></component>
            <component v-if="currentComponent === 'DogsMap'" is="DogsMap"></component>

        </div>
</template>

<script>
    import DogsMap from '../components/DogsMap.vue'
    import SignUp from '../components/SignUp.vue'

    export default{
        components:{
            DogsMap,
            SignUp
        },

        data(){
            return{
                currentComponent:  'Index',

                tabs: [
                    {name: 'SignUp', component: 'SignUp'},
                    {name: 'DogsMap', component: 'DogsMap'}
                ]
            }
        },

        methods:{
            changeTab(tabName){
                this.currentComponent=tabName
            }
        }
    }

</script>