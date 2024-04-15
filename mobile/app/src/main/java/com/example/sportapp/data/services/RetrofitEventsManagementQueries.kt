package com.example.sportapp.data.services

import com.example.sportapp.data.api.EventsService
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import com.example.sportapp.Config
import com.example.sportapp.data.api.CalculateFTPVo2Service
import com.example.sportapp.data.api.ReceiveSesionDataService
import com.example.sportapp.data.api.StartTrainingService
import com.example.sportapp.data.api.StopTrainingService

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

object RetrofitStartTrainingService {

    private const val BASE_URL = Config.BASE_URL_Trainings.toString()

    fun createApiService(): StartTrainingService {
        val retrofit = Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        return retrofit.create(StartTrainingService::class.java)
    }
}

object RetrofitStopTrainingService {

    private const val BASE_URL = Config.BASE_URL_Trainings.toString()

    fun createApiService(): StopTrainingService {
        val retrofit = Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        return retrofit.create(StopTrainingService::class.java)
    }
}

object RetrofitReceiveSesionDataService {

    private const val BASE_URL = Config.BASE_URL_Trainings.toString()

    fun createApiService(): ReceiveSesionDataService {
        val retrofit = Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        return retrofit.create(ReceiveSesionDataService::class.java)
    }
}