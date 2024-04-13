package com.example.sportapp

import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.assertion.ViewAssertions.matches
import androidx.test.espresso.matcher.ViewMatchers.*
import androidx.test.ext.junit.rules.ActivityScenarioRule
import com.example.sportapp.ui.views.StartTraining
import org.junit.Rule
import org.junit.Test

class StartTrainingTest {

    @get:Rule
    val activityScenarioRule = ActivityScenarioRule(StartTraining::class.java)

    @Test
    fun testUIElementsDisplayed() {
        // Verificar que todos los elementos de la interfaz de usuario estén visibles
        onView(withId(R.id.ivHome)).check(matches(isDisplayed()))
        onView(withId(R.id.ivRunExe)).check(matches(isDisplayed()))
        onView(withId(R.id.rvTypeTraining)).check(matches(isDisplayed()))
        onView(withId(R.id.chronometer)).check(matches(isDisplayed()))
        onView(withId(R.id.btnStartTraining)).check(matches(isDisplayed()))
    }

    @Test
    fun testNavigationToHome() {
        // Simular el clic en el icono de inicio
        onView(withId(R.id.ivHome)).perform(click())
        // Verificar que la actividad de inicio (HomeActivity) se haya abierto
        onView(withId(R.id.linearLayout)).check(matches(isDisplayed()))
    }

    @Test
    fun testNavigationToStartTraining() {
        // Simular el clic en el icono de inicio de entrenamiento
        onView(withId(R.id.ivRunExe)).perform(click())
        // Verificar que la actividad de inicio de entrenamiento (StartTraining) se haya abierto
        onView(withId(R.id.linearLayout)).check(matches(isDisplayed()))
    }
}
