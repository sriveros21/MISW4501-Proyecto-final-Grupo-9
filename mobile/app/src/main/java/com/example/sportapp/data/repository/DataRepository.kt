package com.example.sportapp.data.repository

import com.example.sportapp.data.api.EventsService

class DataRepository(private val apiService: EventsService) {
    fun getCalendarEvents(userId: Int) = apiService.getCalendarEvents(userId)
}