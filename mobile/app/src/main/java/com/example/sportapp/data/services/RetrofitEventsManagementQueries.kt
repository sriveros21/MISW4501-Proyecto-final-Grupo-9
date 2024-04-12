package com.example.sportapp.data.services

import com.example.sportapp.data.api.EventsService
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import com.example.sportapp.Config
import android.util.Log

object RetrofitEventsManagementQueries {

    private const val BASE_URL = Config.BASE_URL_Events.toString()

    fun createApiService(): EventsService {
        val retrofit = Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        return retrofit.create(EventsService::class.java)
    }
}