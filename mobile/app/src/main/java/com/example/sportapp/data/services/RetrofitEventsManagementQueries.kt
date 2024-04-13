package com.example.sportapp.data.services

import com.example.sportapp.data.api.EventsService
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import com.example.sportapp.Config
import com.example.sportapp.data.api.CalculateFTPVo2Service

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

object RetrofitCalculateFTPVO2max {

    private const val BASE_URL = Config.BASE_URL_FTPVo2.toString()

    fun createApiService(): CalculateFTPVo2Service {
        val retrofit = Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        return retrofit.create(CalculateFTPVo2Service::class.java)
    }
}