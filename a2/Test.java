
import org.json.*;
import com.thoughtworks.xstream.*;
import java.util.*;
import java.io.*;

public class Test {

   public static void main(String[] args) {
      new Test().doit();
   }

   public void doit() {
      try {

         JSONSearchResultObj json = new JSONSearchResultObj();
         json.setIsStillProcessing(false);

         JSONResult res = new JSONResult();
         res.setCheckboxId("11111");
         res.setClassification("U");
         res.setTitle("Title 1");
         res.setDocUrl("http://www.1.com");
         res.setRelevance("50");
         res.setDocDate("2001-01-01");
         res.setDDMSUrl("http://www.ddms.1");
         JSONProvider prov = new JSONProvider();
         prov.setId("2007-01-01");
         prov.setName("Provider A");
         res.setProvider(prov);
         JSONDescription desc = new JSONDescription();
         desc.setIsTruncated(true);
         desc.setDescription("This is the description 1");
         desc.setTruncated("This is 1");
         res.setDescription(desc);
         json.setResult(res);

         res = new JSONResult();
         res.setCheckboxId("2222");
         res.setClassification("S");
         res.setTitle("Title 2");
         res.setDocUrl("http://www.2.com");
         res.setRelevance("70");
         res.setDocDate("2001-02-02");
         res.setDDMSUrl("http://www.ddms.2");
         prov = new JSONProvider();
         prov.setId("2007-02-02");
         prov.setName("Provider A");
         res.setProvider(prov);
         desc = new JSONDescription();
         desc.setIsTruncated(false);
         desc.setDescription("This is the description 2");
         res.setDescription(desc);
         json.setResult(res);

         JSONStats stat = new JSONStats();
         prov = new JSONProvider();
         prov.setId("2007-01-01");
         prov.setCount("3");
         prov.setProgress("10");
         stat.setProvider(prov);

         prov = new JSONProvider();
         prov.setId("2007-02-02");
         prov.setCount("5");
         prov.setProgress("15");
         stat.setProvider(prov);

         json.setStats(stat);

        String zz = toXML(json);
System.out.println(zz);


      }catch (Exception e) {
         System.out.println("ERROR: " + e.toString());
      }
   }

   /*
    * toObject
   */
   public static Object toObject(String xml) throws Exception {
      XStream xstream = new XStream();
      //xstream.alias("SearchResultObj", SearchResultObj.class);
      return (Object) xstream.fromXML(xml);
   }

   /*
    * toXML
    */
   public static String toXML(Object obj) throws Exception {
      XStream xstream = new XStream();
      xstream.alias("provider", JSONProvider.class);
      xstream.alias("result", JSONResult.class);
      return xstream.toXML(obj); 
   }

   /*
    * toFile
    */
   public static void toFile(Object obj, String file) throws Exception {
      XStream xstream = new XStream();
      //xstream.alias("SearchResultObj", SearchResultObj.class);
      String xml = xstream.toXML(obj); 
      storeToFile(file, xml);
   }

   /*
    * storeToFile
    */
   public static void storeToFile(String file, String data) throws Exception {
      PrintWriter writer = new PrintWriter(
                                     new BufferedWriter(
                                     new FileWriter(file, false)));
      writer.println(data);
      writer.close();
      writer = null;
   }
}
