<template>
        <div>
            <img loading="auto" src="/media/oscar6.png" width="200">
        </div>

        <div class="text-info">
            <h1>HOME PAGE</h1>
        </div>

        <div>
            <div class="tab-buttons">
                <button v-for="(tab, index) in tabs" :key="index" @click="changeTab(tab.name)">
                    {{ tab.name }}
                </button>
            </div>

            <component v-if="currentComponent === 'DogsMap'" is="DogsMap"></component>

        </div>
</template>

<script>
    import DogsMap from '../components/DogsMap.vue'

    export default{
        components:{
            DogsMap
        },

        data(){
            return{
                currentComponent:  'Index',

                tabs: [
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