package com.example.sportapp.data.remote.api

import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Path


interface ApiService {
    @GET("users/{userId}/reset")
    fun sendDataStrava(@Path("userId") userId: String?): Call<Void?>?
}