<template>
    <v-app>
        <v-app-bar
                app
                color="primary"
                dark
        >

            <v-spacer></v-spacer>

            <div class="ma-2">
                <v-btn @click="signUpBtn" color="green" small>SignUp</v-btn>
            </div>
            <div class="ma-2">
                <v-btn @click="loginBtn" color="green" small>Login</v-btn>
            </div>
            <div class="ma-2">
                <v-btn @click="logoutBtn" color="green" small>Logout</v-btn>
            </div>

        </v-app-bar>

        <v-content>
            <v-container>
                <router-view></router-view>

            </v-container>
        </v-content>
    </v-app>
</template>

<script>

    export default {
        name: 'App',


        data: () => ({
            //
        }),
        methods: {
            logoutBtn() {
                this.$http.logout()
            },
            loginBtn() {
                this.$router.push('/login').catch(err => {})
            },
            signUpBtn() {
                this.$router.push('/signup')
            }
        }
    };
</script>
