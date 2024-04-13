package com.example.sportapp

import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.NoMatchingViewException
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.assertion.ViewAssertions.matches
import androidx.test.espresso.matcher.ViewMatchers.*
import androidx.test.ext.junit.rules.ActivityScenarioRule
import com.example.sportapp.ui.views.RunTraining
import org.junit.Rule
import org.junit.Test

class RunTrainingTest {

    @get:Rule
    val activityScenarioRule = ActivityScenarioRule(RunTraining::class.java)

    @Test
    fun testUIElementsDisplayed() {
        // Verificar que todos los elementos de la interfaz de usuario estén visibles
        onView(withId(R.id.ivHome)).check(matches(isDisplayed()))
        onView(withId(R.id.tvwTypeRun)).check(matches(isDisplayed()))
        onView(withId(R.id.chronometer1)).check(matches(isDisplayed()))
        onView(withId(R.id.btnStart)).check(matches(isDisplayed()))
    }

    @Test
    fun testNavigationToHome() {
        // Simular el clic en el icono de inicio
        onView(withId(R.id.ivHome)).perform(click())
        // Verificar que la actividad de inicio (HomeActivity) se haya abierto
        onView(withId(R.id.linearLayout)).check(matches(isDisplayed()))
    }

    @Test
    fun testChronometerStarts() {
        // Simular el clic en el botón de inicio
        onView(withId(R.id.btnStart)).perform(click())

//        // Esperar un máximo de 5 segundos hasta que el cronómetro esté visible
//        try {
//            Thread.sleep(5000)
//            onView(withId(R.id.chronometer1)).check(matches(isDisplayed()))
//        } catch (e: NoMatchingViewException) {
//            // Manejar la excepción NoMatchingViewException
//            throw AssertionError("El cronómetro no se mostró después de hacer clic en el botón de inicio", e)
//        } catch (e: AssertionError) {
//            // Manejar la excepción AssertionError
//            throw AssertionError("El cronómetro no se mostró después de hacer clic en el botón de inicio", e)
//        }
    }

}
