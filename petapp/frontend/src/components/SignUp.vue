<template>
    <div v-html="signup"></div>
</template>

<script>
    export default {
        data() {
        return {
            signup: '',
        };
        },
        async created() {
        const response = await fetch('signup');
        const data = await response.text();
        this.signup = data;
        },
    };
</script>
