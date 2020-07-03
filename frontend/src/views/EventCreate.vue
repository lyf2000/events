<template>
    <div class="event-create">

        <v-dialog
                v-model="dialog2"
                width="500"
        >

            <v-card>
                <v-card-title
                        class="headline grey lighten-2"
                        primary-title
                >Error!
                </v-card-title>

                <v-card-text >{{errorMessage}}
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                            color="primary"
                            text
                            @click="dialog2 = false"
                    >
                        I accept
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

        <v-card>
            <v-card-title>
                <span class="headline">Create Event</span>
            </v-card-title>
            <v-card-text>
                <v-container>
                    <v-row>


                        <v-col cols="4">
                            <v-text-field placeholder="Title" v-model="event.title"></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-textarea placeholder="Text" v-model="event.text"></v-textarea>
                        </v-col>

                        <v-col cols="2">
                            <v-menu
                                    v-model="menu2"
                                    :close-on-content-click="false"
                                    transition="scale-transition"
                                    offset-y
                            >
                                <template v-slot:activator="{ on, attrs }">
                                    <v-text-field
                                            v-model="computedDateFormatted"
                                            label="Date"
                                            persistent-hint
                                            readonly
                                            v-bind="attrs"
                                            v-on="on"
                                    ></v-text-field>
                                </template>
                                <v-date-picker v-model="event.date" no-title @input="menu2 = false"></v-date-picker>
                            </v-menu>
                        </v-col>
                        <v-col cols="4">
                            <v-menu
                                    ref="menu3"
                                    v-model="menu3"
                                    :close-on-content-click="false"
                                    :nudge-right="40"
                                    :return-value.sync="event.time"
                                    transition="scale-transition"
                                    offset-y
                            >
                                <template v-slot:activator="{ on, attrs }">
                                    <v-text-field
                                            v-model="event.time"
                                            label="Time"
                                            readonly
                                            v-bind="attrs"
                                            v-on="on"
                                    ></v-text-field>
                                </template>
                                <v-time-picker
                                        v-if="menu3"
                                        v-model="event.time"
                                        transition="scale-transition"
                                        full-width
                                        format="24hr"
                                        @click:minute="$refs.menu3.save(event.time)"
                                ></v-time-picker>
                            </v-menu>
                        </v-col>
                    </v-row>
                </v-container>
                <small>*indicates required field</small>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDialog">Close</v-btn>
                <v-btn color="blue darken-1" text @click="createEvent">Save</v-btn>
            </v-card-actions>
        </v-card>

        <v-row>


        </v-row>


    </div>
</template>

<script>

    export default {
        name: "PostCreate",
        props: {
            event: Object,
        },
        data() {
            return {
                ob: {
                    text: '',
                    title: '',
                    date: '',
                    time: '',
                },
                dialog2: false,
                errorMessage: '',
                dateFormatted: '',
                menu2: false,
                menu3: false,
            }
        },
        computed: {
            computedDateFormatted() {
                return this.formatDate(this.event.date)
            },
        },

        methods: {

            formatDate(date) {
                if (!date) return null

                const [year, month, day] = date.split('-')
                return `${year}-${month}-${day}`
            },
            parseDate(date) {
                if (!date) return null

                const [month, day, year] = date.split('/')
                return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
            },

            axiosPost(url, data = {}) {
                return this.$http.post(url, data)
            },
            axiosGet(url) {
                return this.$http.get(url)
            },
            createEvent() {
                const self = this;

                let formData = new FormData();
                formData.append("title", self.event.title);
                formData.append("text", self.event.text);
                formData.append("date", `${self.event.date} ${self.event.time}`);

                if (self.event.put) {
                    self.$http.put(`/events/${self.event.id}/`, formData)
                        .then(function (response) {
                            self.clearForm();
                            self.$emit('new-event')
                        })
                        .catch(response => {
                            console.log(response.response.data)
                            self.errorEventCreate(response.response.data)
                        })
                } else {
                    self.$http.post('/events/', formData)
                        .then(function (response) {
                            self.clearForm();
                            self.$emit('new-event')
                        })
                        .catch(response => {
                            console.log(response.response.data)
                            self.errorEventCreate(response.response.data)
                        })
                }


            },
            errorEventCreate(data) {
                console.log(data)
                let m = ''
                for (const [key, value] of Object.entries(data)) {
                    m += `${key}: ${value.join(', ')}`
                }
                console.log('m', m)
                this.errorMessage = m
                this.dialog2 = true
            },
            clearForm() {
                this.event.text = ''
                this.event.title = ''
                this.event.date = ''
                this.event.time = ''
            },
            closeDialog() {
                this.clearForm()
                this.$emit('close-dialog')
            }
        },
    }
</script>

<style scoped>

</style>