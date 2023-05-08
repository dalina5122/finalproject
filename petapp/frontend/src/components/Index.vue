<template>
    <div class="container">
      <div class="p-2">
        <!-- CREATE ACCOUNT -->
        <div>
            <h4>Would you like to create an account?</h4>
            <router-link to="/signup">
                <img loading="auto" src="/media/signup.png" width="100">
            </router-link>
        </div>

        <!-- LOG IN -->
        <div>
            <h4>Already have an account?</h4>
            <router-link to="/log-in">
                <img loading="auto" src="/media/login.png" width="100">
            </router-link>
        </div>

        <!-- ARROW FOR SCROLLING DOWN -->
        <div>
            <button class="scroll-down" @click="scrollDown">
                <img loading="auto" src="/media/arrow.gif" width="100">
            </button>
        </div>
      </div>
    </div>

    <!-- INTRODUCTION -->
    <div>
        <img class="intro" loading="auto" src="/media/intro.png" width="1200">

        <button class="btn btn-outline-info my-2 my-sm-0" @click="scrollUp"> Would you like to get started? </button>
    </div>
</template>

<script>
    export default{
        methods:{
            scrollDown() {
                window.scrollTo({
                    top: document.body.scrollHeight,
                    behavior: 'smooth',
                });
            },

            scrollUp(){
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth',
                })
            }
        }
    }
</script>

<style scoped>
.intro{
    margin-top: 200px;
}

.scroll-down{
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
}
</style>






