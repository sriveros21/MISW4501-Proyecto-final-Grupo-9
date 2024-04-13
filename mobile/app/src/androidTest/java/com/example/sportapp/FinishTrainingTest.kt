package com.example.sportapp
import androidx.test.espresso.Espresso
import androidx.test.espresso.action.ViewActions
import androidx.test.espresso.assertion.ViewAssertions
import androidx.test.espresso.matcher.ViewMatchers
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import com.example.sportapp.ui.views.FinishTraining
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class FinishTrainingTest {

    @get:Rule
    val activityScenarioRule = ActivityScenarioRule(FinishTraining::class.java)

    @Test
    fun testUIElementsDisplayed() {
        // Verificar que todos los elementos de la interfaz de usuario estén visibles
        Espresso.onView(ViewMatchers.withId(R.id.ivHome)).check(ViewAssertions.matches(ViewMatchers.isDisplayed()))
        Espresso.onView(ViewMatchers.withId(R.id.ivRunExe)).check(ViewAssertions.matches(ViewMatchers.isDisplayed()))
        Espresso.onView(ViewMatchers.withId(R.id.tvwType)).check(ViewAssertions.matches(ViewMatchers.isDisplayed()))
        Espresso.onView(ViewMatchers.withId(R.id.tvwTimeTotal)).check(ViewAssertions.matches(ViewMatchers.isDisplayed()))
        Espresso.onView(ViewMatchers.withId(R.id.tvwDateTraining)).check(ViewAssertions.matches(ViewMatchers.isDisplayed()))
        Espresso.onView(ViewMatchers.withId(R.id.tvwCalTraining)).check(ViewAssertions.matches(ViewMatchers.isDisplayed()))
        Espresso.onView(ViewMatchers.withId(R.id.tvwFTP)).check(ViewAssertions.matches(ViewMatchers.isDisplayed()))
        Espresso.onView(ViewMatchers.withId(R.id.tvwVO2)).check(ViewAssertions.matches(ViewMatchers.isDisplayed()))
        Espresso.onView(ViewMatchers.withId(R.id.btnStart)).check(ViewAssertions.matches(ViewMatchers.isDisplayed()))
    }

    @Test
    fun testNavigationToHome() {
        // Simular el clic en el icono de inicio
        Espresso.onView(ViewMatchers.withId(R.id.ivHome)).perform(ViewActions.click())
        // Verificar que la actividad de inicio (Home) se haya abierto
        Espresso.onView(ViewMatchers.withId(R.id.linearLayout)).check(ViewAssertions.matches(ViewMatchers.isDisplayed()))
    }

    @Test
    fun testNavigationToStartTraining() {
        // Simular el clic en el icono de inicio de entrenamiento
        Espresso.onView(ViewMatchers.withId(R.id.ivRunExe)).perform(ViewActions.click())
        // Verificar que la actividad de inicio de entrenamiento (StartTraining) se haya abierto
        Espresso.onView(ViewMatchers.withId(R.id.linearLayout)).check(ViewAssertions.matches(ViewMatchers.isDisplayed()))
    }
}
