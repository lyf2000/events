<template>


    <v-card
            class="mx-auto"
            color="#26c6da"
            dark
            width="60%"
    >
        <v-card-title>
            <v-icon
                    large
                    left
            >
                mdi-done
            </v-icon>
            <span class="title font-weight-light">{{event.title}}</span>
        </v-card-title>

        <v-card-text class="headline font-weight-bold">
            {{event.text}}
        </v-card-text>

        <v-card-actions>
            <v-list-item class="grow">

                <v-list-item-content>
                    <v-list-item-title>{{event.date}}</v-list-item-title>
                </v-list-item-content>

                <v-row
                        align="center"
                        justify="end"
                >
                    <v-btn icon
                        @click="$emit('change-event', event.id)"
                    >
                        <v-icon class="mr-1">mdi-fountain-pen</v-icon>
                    </v-btn>

                    <v-btn icon
                        @click="deleteEvent(event.id)"
                    >
                        <v-icon class="mr-1">mdi-delete</v-icon>
                    </v-btn>
                </v-row>
            </v-list-item>
        </v-card-actions>
    </v-card>


</template>

<script>
    export default {
        name: "EventCard",
        props: {
            event: {
                type: Object,
            }
        },
        methods: {
            goToEvent() {
                const self = this;
                console.log(self.event.id);
                this.$router.push('/event/' + self.event.id)
            },
            deleteEvent(id) {
                const self = this;
                console.log(id)
                // let formData = new FormData();
                // formData.append("id", id);
                self.$http.delete(`events/${id}/`)
                    .then(response => {
                        this.$emit('deleteEvent', id)
                    })
                    .catch(response => {
                        console.log(response.response.data)
                    })
            }
        },
    }
</script>

<style scoped>

</style>