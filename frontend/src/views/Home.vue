<template>
    <div class="home">
        <EventCardList/>
    </div>
</template>

<script>

    import EventCardList from '@/components/home/EventCardList.vue'

    export default {
        name: 'Home',
        props: ['id'],
        components: {
            EventCardList,
        },
        data() {
            return {

            }
        },
        methods: {

        },
        created() {

        }
    }
</script>
