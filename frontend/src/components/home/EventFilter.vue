<template>
    <v-row>
        <v-col
                cols="12"
                sm="2"
        >
            <v-text-field
                    v-on:keypress.enter="filterEvents"
                    v-model="searchText"
                    label="Search"
                    :filled="true"
            ></v-text-field>
        </v-col>
        <v-col
                cols="12"
                sm="2"
        >
            <v-select
                    filled
                    :items="period"
                    label="Select for the last"
                    v-model="periodSelected"
                    v-on:change="filterEvents"
            ></v-select>
        </v-col>

        <v-col  sm="2">

            <div class="ma-2">
                <v-btn :disabled="!prev"
                       depressed
                       small
                       @click="$emit('prev-page')"
                >
                    <v-icon>mdi-chevron-left</v-icon>
                </v-btn>
                <v-btn :disabled="!next"
                       depressed
                       small
                       @click="$emit('next-page')"
                >
                    <v-icon>mdi-chevron-right</v-icon>
                </v-btn>
            </div>
        </v-col>

    </v-row>
</template>

<script>

    export default {
        name: "EventFilter",
        props: {
            next: null,
            prev: null
        },
        data() {
            return {
                searchText: "",
                orderValues: ['Asc', "Desc"],
                orderSelected: 'Desc',
                period: ['day', 'week', 'month', 'all'],
                periodSelected: '',
            }
        },
        methods: {
            getSearchParams() {
                let self = this;
                return {
                    'search': self.searchText.trim(),
                    'ordering': self.getOrderValue(),
                    'period': self.periodSelected,

                }
            },
            getOrderValue() {
                let self = this;
                let order = "-created";
                if (self.orderSelected === "Asc") {
                    order = "created"
                }
                return order
            },
            filterEvents() {
                const searchParams = decodeURIComponent(new URLSearchParams(this.getSearchParams()).toString());
                this.$emit('filter-events', searchParams);
            },
        },
    }
</script>

<style scoped>

</style>