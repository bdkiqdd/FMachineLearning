// Imports
import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

// Declaração de Constante para utilização do Navigator
const AppStack = createStackNavigator();

// Import da página
import Home from "./pages/Home.js";

// Declaração de rota para Home 
export default function Routes(){
    return (
        <NavigationContainer>
            <AppStack.Navigator screenOptions={{ headerShown: false }}>
                <AppStack.Screen name = "Home" component = {Home}/>
            </AppStack.Navigator>
        </NavigationContainer>
    );
}