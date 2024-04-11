package com.example.sportapp.data.services

import com.example.sportapp.data.api.EventsService
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitEventsManagementQueries {
    private const val BASE_URL = "http://127.0.0.1:3002/"

//    val instance: EventsService by lazy {
//        val retrofit = Retrofit.Builder()
//            .baseUrl(BASE_URL)
//            .addConverterFactory(GsonConverterFactory.create())
//            .build()
//
//        retrofit.create(EventsService::class.java)
//    }

    fun createApiService(): EventsService {
        val retrofit = Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        return retrofit.create(EventsService::class.java)
    }
}