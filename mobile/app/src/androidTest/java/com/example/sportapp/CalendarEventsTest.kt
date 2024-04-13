package com.example.sportapp
import androidx.recyclerview.widget.RecyclerView
import androidx.test.espresso.Espresso
import androidx.test.espresso.ViewAssertion
import androidx.test.espresso.action.ViewActions
import androidx.test.espresso.matcher.ViewMatchers
import androidx.test.espresso.matcher.ViewMatchers.assertThat
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.filters.LargeTest
import com.example.sportapp.ui.views.CalendarEvents
import org.hamcrest.CoreMatchers.`is`
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
@LargeTest
class CalendarEventsTest {

    @get:Rule
    val activityScenarioRule = ActivityScenarioRule(CalendarEvents::class.java)

//    @Test
//    fun testRecyclerViewItemCount() {
//        // Verifica que el RecyclerView contenga al menos un elemento
//        Espresso.onView(ViewMatchers.withId(R.id.rvEvents))
//            .check(RecyclerViewItemCountAssertion.hasItemCount(1))
//    }

    @Test
    fun testNavigationClick() {
        // Haz clic en el icono de inicio
        Espresso.onView(ViewMatchers.withId(R.id.ivHome))
            .perform(ViewActions.click())
        // Agrega aquí aserciones adicionales según el comportamiento esperado después de hacer clic en el icono de inicio
    }

    object RecyclerViewItemCountAssertion {

        fun hasItemCount(expectedCount: Int): ViewAssertion {
            return ViewAssertion { view, noViewFoundException ->
                if (noViewFoundException != null) {
                    throw noViewFoundException
                }

                if (view is RecyclerView) {
                    val adapter = view.adapter
                    assertThat(adapter?.itemCount, `is`(expectedCount))
                } else {
                    throw IllegalArgumentException("The asserted view is not a RecyclerView")
                }
            }
        }
    }
}