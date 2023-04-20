<template>
        <div>
            <img loading="auto" src="/media/oscar6.png" width="200">
        </div>

        <div class="text-info">
            <h1>HOME PAGE</h1>
        </div>

        <button
            v-for="tab in tabs"
            :key="tab"
            :class="['tab-button', { active: currentTab === tab }]"
            @click="currentTab=tab">
            {{ tab }}
        </button>

        <component :is="currentTab.component" class="tab"></component>
</template>

<script>
    import DogsMap from '../components/DogsMap.vue'

    export default{
        components:{
            DogsMap
        },

        data(){
            return{
                currentTab: {
                    name: 'Index',
                    component: null
                },

                tabs: [
                    {name: 'DogsMap', path: '../components/DogsMap.vue'}
                ]
            }
        },

        methods:{
            async loadComponent(name){
                const component = await import(this.tabs.find(tab => tab.name === name).path)
                this.currentTab.component = component.default
            },


            created() {
                this.loadComponent(this.currentTab.name)
            }
        }
    }

</script>