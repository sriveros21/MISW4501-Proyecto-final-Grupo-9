package com.example.sportapp.data.api

import com.example.sportapp.data.model.CalendarEvent
import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Path


interface EventsService {
    @GET("/user/{userId}/calendar")
    fun getCalendarEvents(@Path("userId") userId: Int): Call<List<CalendarEvent>>
}

