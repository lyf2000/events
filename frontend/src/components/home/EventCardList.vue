<template>
    <div>
        <v-container>

            <v-btn
                    color="primary"
                    dark
                    @click.stop="openEmptyDialoge"
            >Create Event
            </v-btn>

            <v-dialog
                    v-model="dialog"
                    width="60%"
            >

                <EventCreate
                        v-bind:event="currentEvent"
                        @new-event="addEvent"
                        @close-dialog="dialog = false"
                />

            </v-dialog>

            <EventFilter
                    @filter-events="filterEvents"
                    @prev-page="prevPage"
                    @next-page="nextPage"
                    v-bind:next="next"
                    v-bind:prev="prev"
            />
            <EventCardItem
                    v-for="event of events"
                    @change-event="changeEvent"
                    v-bind:event="event"
                    @deleteEvent="deleteEvent"
            />
        </v-container>
    </div>
</template>

<script>

    import EventCardItem from "./EventCardItem";
    import EventFilter from "./EventFilter";
    import EventCreate from "../../views/EventCreate";

    export default {
        name: "EventCardList",
        data() {
            return {
                events: [],
                next: null,
                prev: null,
                dialog: false,
                currentEvent: {
                    text: '',
                    title: '',
                    date: '',
                    time: '',
                }
            }
        },
        components: {
            EventCreate,
            EventCardItem, EventFilter
        },
        methods: {

            loadEvents() {
                this.filterEvents("")
            },
            f() {
                console.log(123);
            },
            axiosGet(url) {
                return this.$http.get(url)
            },
            otherPage(url) {
                const self = this;
                self.axiosGet(url)
                    .then(function (response) {
                        self.newEvents(response);
                    })
            },
            newEvents(response) {
                const {results, next, previous} = response.data

                this.events = results;
                this.next = next;
                this.prev = previous
            },
            filterEvents(searchParams) {
                const self = this;
                const url = '/events/?' + searchParams;
                self.axiosGet(url)
                    .then(function (response) {
                        self.newEvents(response)
                    })
            },
            prevPage() {
                if (this.prev) {
                    this.otherPage(this.prev)
                }
            },
            nextPage() {
                if (this.next) {
                    this.otherPage(this.next)
                }
            },
            deleteEvent(id) {
                this.loadEvents()
            },
            addEvent() {
                this.dialog = false
                this.loadEvents()
            },
            changeEvent(id) {
                this.currentEvent = Object.assign({}, this.events.filter(event => event.id === id)[0])
                const dt = this.currentEvent.date.split(' ')
                this.currentEvent.date = dt[0]
                this.currentEvent.time = dt[1]
                this.currentEvent['put'] = true
                this.dialog = true
            },
            openEmptyDialoge() {
                this.currentEvent = {
                    text: '',
                    title: '',
                    date: '',
                    time: '',
                }
                this.dialog = true
            }

        },
        created() {
            this.loadEvents();
        },

    }
</script>

<style scoped>

</style>