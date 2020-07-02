<template>
    <v-form
            ref="form"
            v-model="valid"
            :lazy-validation="lazy"
    >
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
                            alert('Inputs are wrong!')
                        })
                }
            }
        }
    }


</script>

<style scoped>

</style>