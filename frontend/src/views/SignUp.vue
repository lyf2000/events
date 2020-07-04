<template>

    <v-form
            ref="form"
            v-model="valid"
            :lazy-validation="lazy"
    >

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
                        OK
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

        <v-text-field
                v-model="form.username"
                :rules="usernameRules"
                label="Username"
                required
        ></v-text-field>

        <v-text-field
                v-model="form.email"
                :rules="emailRules"
                label="E-mail"
                required
        ></v-text-field>

        <v-text-field
                type="password"
                v-model="form.password"
                :rules="passwordRules"
                label="Password"
                required
        ></v-text-field>

        <v-btn
                :disabled="!valid"
                color="success"
                class="mr-4"
                @click="signUp"
        >
            Validate
        </v-btn>

    </v-form>
</template>

<script>
    export default {
        name: "SignUp",
        data: () => ({
            dialog2: false,
            errorMessage: '',
            valid: true,
            form: {
                username: '',
                email: '',
                password: '',
            },
            lazy: false,
            usernameRules: [
                v => !!v || 'Username is required',
            ],
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],
            passwordRules: [
                v => !!v || 'Password is required',
            ],
        }),

        methods: {
            validate() {
                this.$refs.form.validate()
            },
            signUp() {
                const self = this
                if (self.valid) {
                    const form_data = new FormData();

                    for (let key in self.form) {
                        form_data.append(key, self.form[key]);
                    }

                    self.$http.post('/signup', form_data)
                        .then(response => {
                            self.$router.push('/login')
                        })
                        .catch(response => {
                            self.errorEventCreate(response.response.data)
                        })
                }
            },
            errorEventCreate(data) {
                console.log(data)
                let m = ''
                for (const [key, value] of Object.entries(data)) {
                    m += `${key}: ${value}`
                }
                console.log('m', m)
                this.errorMessage = m
                this.dialog2 = true
            },
        }
    }


</script>

<style scoped>

</style>